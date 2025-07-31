from functools import wraps
from flask_login import current_user
from flask import redirect, url_for, flash

def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("Please log in first.", "warning")
            return redirect(url_for("auth.admin_login"))

        if not current_user.is_admin():
            flash("You do not have permission to access this page.", "danger")
            return redirect(url_for("main.index"))

        return func(*args, **kwargs)

    return decorated_view