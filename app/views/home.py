import base64
import os.path

import cv2
from flask import render_template, Blueprint, request, redirect, url_for
from werkzeug.utils import secure_filename

from app import app
from app.controllers import allowed_file, predict_on_image
from ultralytics import YOLO

bp = Blueprint("home", __name__, template_folder="../templates")

model = YOLO("yolov8n.pt")


@bp.route("/", methods=["GET", "POST"])
def Index():
    if request.method == "POST":
        if 'file' not in request.files:
            return render_template("home.html", error="File could not found")
        file = request.files['file']
        if file == '':
            return render_template("home.html", error="No selected file")
        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)
            file.save(os.path.join(app.UPLOAD_FOLDER,filename))


            predicted_image = predict_on_image(filename)

            retval, buffer = cv2.imencode('.png', predicted_image)
            detection_img_base64 = base64.b64encode(buffer).decode('utf-8')

            file.stream.seek(0)
            original_img_base64 = base64.b64encode(file.stream.read()).decode('utf-8')

            return render_template('result.html', original_img_data=original_img_base64,
                                   detection_img_data=detection_img_base64)

    return render_template("home.html")
