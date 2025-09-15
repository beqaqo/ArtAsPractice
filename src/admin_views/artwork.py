from flask_admin.form import ImageUploadField
from src.admin_views.base import SecureModelView
from src.config import Config
from src.models.artwork import Artwork, ArtworkImage
from os import path
from uuid import uuid4
from markupsafe import Markup


def generate_filename(obj, file):
    name, extension = path.splitext(file.filename)
    return f"{uuid4()}{extension}"

class ArtworkView(SecureModelView):
    inline_models = [
        (ArtworkImage, dict(
            form_overrides={'image_name': ImageUploadField},
            form_args={
                'image_name': {
                    'label': 'Image',
                    'base_path': Config.UPLOAD_PATH,
                    'namegen': generate_filename,
                    'allow_overwrite': False
                }
            },
            form_label="Images"
        ))
    ]

    column_list = (
        "author", "name", "series", "style", "size", "price", "link", "images_preview"
    )
    column_editable_list = ("author", "name", "series", "style", "size", "price")
    column_searchable_list = ("author", "name", "series", "style")
    column_filters = ("author", "series", "style")
    form_columns = ("author", "name", "description", "series", "size", "style", "price", "link", "images")

    column_formatters = {
        "price": lambda v, c, m, p: f"${m.price:,.2f}" if m.price else "",
        "images_preview": lambda v, c, m, p: Markup(
            f'<img src="/static/uploads/{m.images[0].image_name}" width="50">'
            if m.images else ""
        )
    }
