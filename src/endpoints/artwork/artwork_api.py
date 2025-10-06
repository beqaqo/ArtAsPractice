from flask_restx import Resource, reqparse
from src.models import Artwork
from src.endpoints.artwork import artwork_ns, artwork_model

pagination_parser = reqparse.RequestParser()
pagination_parser.add_argument('page', type=int, default=1)
pagination_parser.add_argument('limit', type=int, default=2)

@artwork_ns.route("/")
class ArtworkApi(Resource):

    @artwork_ns.expect(pagination_parser)
    @artwork_ns.marshal_with(artwork_model, as_list=True)
    def get(self):
        args = pagination_parser.parse_args()
        page = args['page']
        limit = args['limit']
        offset = (page - 1) * limit

        artworks = Artwork.query.offset(offset).limit(limit).all()

        for artwork in artworks:
            for img in artwork.images:
                img.image_name = f"/static/uploads/{img.image_name}"

        return artworks


@artwork_ns.route("/<int:id>")
class ArtworkDetailApi(Resource):
    @artwork_ns.marshal_with(artwork_model)
    def get(self, id):
        artwork = Artwork.query.get_or_404(id)
        for img in artwork.images:
            img.image_name = f"/static/uploads/{img.image_name}"

        return artwork


