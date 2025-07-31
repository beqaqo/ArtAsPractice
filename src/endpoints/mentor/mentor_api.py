from flask_restx import Resource
from src.models import Mentor
from src.endpoints.mentor import mentor_ns, mentor_model

@mentor_ns.route("/")
class MentorApi(Resource):

    @mentor_ns.marshal_with(mentor_model)
    def get(self):
        mentors = Mentor.query.all()
        return mentors
