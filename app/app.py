from flask import Flask
from .views import home
import os
UPLOAD_FOLDER = "uploads"
ROOT_DIR = os.path.abspath("../"+os.curdir)

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['ROOT_DIR'] = ROOT_DIR
    #app.config.from_pyfile("config.py")
    app.register_blueprint(home.bp)
    return app
