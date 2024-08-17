from flask import Flask
from .views import home


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    #app.config.from_pyfile("config.py")
    app.register_blueprint(home.bp)
    return app
