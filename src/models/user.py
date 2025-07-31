from src.ext import db
from flask_login import UserMixin
from src.models.base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    _password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, default="User")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_admin(self):
        return self.role == "Admin"

    @property
    def password(self):
        print("GETTER")
        return self._password

    @password.setter
    def password(self, password):
        print("SETTER")
        self._password = generate_password_hash(password)