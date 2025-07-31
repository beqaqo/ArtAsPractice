from src.ext import api
from flask_restx import fields

mentor_ns = api.namespace("Mentors", description="Mentors API")

mentor_model = api.model("Mentor", {
    "id": fields.Integer,
    "name": fields.String,
    "about": fields.String,
    "photo": fields.String,
})