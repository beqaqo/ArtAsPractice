from flask import Flask
from src.config import Config
from src.ext import db, migrate
from src.commands import init_db, populate_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.cli.add_command(init_db)
    app.cli.add_command(populate_db)

    @app.route("/")
    def index():
        return "Hello World!"

    return app
