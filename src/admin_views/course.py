from flask_admin.form import ImageUploadField
from flask_admin.contrib.sqla.fields import QuerySelectField
from src.admin_views.base import SecureModelView
from src.config import Config
from src.models import Mentor
from os import path
from uuid import uuid4


def generate_filename(obj, file):
    name, extension = path.splitext(file.filename)
    return f"{uuid4()}{extension}"

class CourseView(SecureModelView):
    create_modal = True
    edit_modal = True

    column_list = ('title', 'description', 'type', 'price', 'mentor')
    column_editable_list = ("title", "description", "type", "price")
    column_filters = ("mentor", "type")
    column_exclude_list = ("photo",)

    form_overrides = {
        'photo': ImageUploadField
    }
    form_args = {
        "photo": {
            "base_path": Config.UPLOAD_PATH,
            "namegen": generate_filename
        }
    }

    form_columns = ('title', 'description', 'type', 'price', 'mentor', 'photo')

    form_extra_fields = {
        'mentor': QuerySelectField(
            'Mentor',
            query_factory=lambda: Mentor.query.all(),
            get_label='name'
        )
    }

    column_formatters = {
        "description": lambda v, c, m, p: m.description[:250] + "..." if m.description and len(m.description) > 250 else m.description,
        "mentor": lambda v, c, m, p: m.mentor.name if m.mentor else ""
    }
