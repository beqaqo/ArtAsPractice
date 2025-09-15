from src.ext import api
from flask_restx import fields
from src.endpoints.mentor.mentor_api import mentor_model

artwork_ns = api.namespace("Artworks", description="Artworks API")

artwork_image_model = api.model("ArtworkImage", {
    "id": fields.Integer,
    "image_name": fields.String,
})

artwork_model = api.model("Artwork", {
    "id": fields.Integer,
    "author": fields.String(required=True),
    "name": fields.String(required=True),
    "description": fields.String,
    "series": fields.String,
    "size": fields.String,
    "style": fields.String,
    "price": fields.Float,
    "link": fields.String,

    "images": fields.List(fields.Nested(artwork_image_model))
})