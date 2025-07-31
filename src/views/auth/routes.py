from flask import Blueprint, render_template, redirect, request, flash, url_for
from src.views.auth.forms import AdminLoginForm
from src.models import User
from flask_login import login_user, logout_user, login_required, current_user

auth_blueprint = Blueprint("auth", __name__, url_prefix="/admin")

@auth_blueprint.route("/login", methods=["GET", "POST"])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.index"))

    form = AdminLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Success!", "success")
            next_page = request.args.get("next")
            return redirect(next_page or url_for("admin.index"))
        else:
            flash("Wrong password or surname", "danger")

    return render_template("auth/login.html", form=form)


@auth_blueprint.route("/logout")
@login_required
def admin_logout():
    logout_user()
    flash("Logout", "info")
    return redirect(url_for("auth.admin_login"))
