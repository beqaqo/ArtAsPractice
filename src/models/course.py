from src.ext import db
from src.models.base import BaseModel


class Course(BaseModel):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    photo = db.Column(db.String, nullable=False)

    mentor_id = db.Column(db.Integer, db.ForeignKey("mentors.id"))
    mentor = db.relationship("Mentor", back_populates="courses")