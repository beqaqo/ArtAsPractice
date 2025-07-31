from flask_restx import Resource
from src.models import Course
from src.endpoints.course import course_ns, course_model

@course_ns.route("/")
class CourseApi(Resource):

    @course_ns.marshal_with(course_model)
    def get(self):
        courses = Course.query.all()
        return courses
