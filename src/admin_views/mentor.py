from flask_admin.form import ImageUploadField
from src.admin_views.base import SecureModelView
from src.config import Config
from os import path
from uuid import uuid4

def generate_filename(obj, file):
    name, extension = path.splitext(file.filename)
    return f"{uuid4()}{extension}"

class MentorView(SecureModelView):
    can_create = True
    can_edit = False
    can_delete = False
    can_view_details = True
    create_modal = True
    edit_modal = True
    column_details_list = ["name", "about", "photo"]
    column_searchable_list = ["name"]
    column_exclude_list = ("photo",)
    column_formatters = {
        "about": lambda v, c, m, n: m.about if len(m.about) <= 250 else m.about[:250] + "...",
    }
    form_overrides = {
        'photo': ImageUploadField
    }

    form_args = {
        "photo": {
            "base_path": Config.UPLOAD_PATH,
            "namegen": generate_filename,
        }
    }