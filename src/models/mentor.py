from src.ext import db
from src.models.base import BaseModel

class Mentor(BaseModel):
    __tablename__ = "mentors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    about = db.Column(db.String, nullable=False)
    photo = db.Column(db.String, nullable=False)

    courses = db.relationship("Course", back_populates="mentor")