from flask import Flask
from flask_admin.menu import MenuLink

from src.admin_views import MentorView, CourseView, ArtworkView
from src.config import Config
from src.ext import db, migrate, api, admin, login_manager
from src.commands import init_db, populate_db
from src.models.artwork import Artwork
from src.models.course import Course
from src.models.mentor import Mentor
from src.models.user import User

from src.endpoints.course.course_api import CourseApi
from src.endpoints.mentor.mentor_api import MentorApi
from src.views.auth.routes import auth_blueprint

COMMANDS = [init_db, populate_db]
BLUEPRINTS = [auth_blueprint]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.admin_login"
    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)

    admin.init_app(app)
    admin.add_view(MentorView(Mentor, db.session))
    admin.add_view(CourseView(Course, db.session))
    admin.add_view(ArtworkView(Artwork, db.session))
    admin.add_link(MenuLink("Logout", url="/admin/logout"))

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)