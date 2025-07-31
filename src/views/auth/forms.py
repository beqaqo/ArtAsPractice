from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired


class AdminLoginForm(FlaskForm):
    username = StringField(
        "Enter username",
        validators=[DataRequired(message="Username is required")])
    password = PasswordField(
        "Enter password",
        validators=[DataRequired(message="Password is required")])
    login = SubmitField("Login")