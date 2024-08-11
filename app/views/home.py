from flask import render_template, Blueprint, request

bp = Blueprint("home", __name__, template_folder="../templates")


@bp.route("/", methods=["GET", "POST"])
def Index():
    if request.method == "POST":
        if request.form:


    return render_template("index.html")
