from src.ext import api
from flask_restx import fields
from src.endpoints.mentor.mentor_api import mentor_model

course_ns = api.namespace("Courses", description="Courses API")

course_model = api.model("Course", {
    "id": fields.Integer,
    "title": fields.String,
    "description": fields.String,
    "type": fields.String,
    "price": fields.Float,
    "mentor_id": fields.Integer,
    "mentor": fields.Nested(mentor_model)
})