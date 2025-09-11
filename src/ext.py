from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_login import LoginManager
from flask_admin import Admin
from src.admin_views.base import SecureIndexView

db = SQLAlchemy()
migrate = Migrate()
api = Api(title="Art As Practice - API")
login_manager = LoginManager()
admin = Admin(template_mode="bootstrap4", index_view=SecureIndexView())