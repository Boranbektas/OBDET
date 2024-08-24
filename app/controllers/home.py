import cv2
import numpy as np
from ultralytics import YOLO
from app import app

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
model = YOLO("yolov8n.pt")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def predict_on_image(filename):
    filepath = app.UPLOAD_FOLDER +"/"+filename
    image = cv2.imread(filepath,cv2.IMREAD_COLOR)
    print(image.shape)
    results = model.predict(filepath, conf=0.5)
    for i, r in enumerate(results):
        im_bgr = r.plot()


    cv2.imwrite("Pred"+filename,im_bgr)
    return im_bgr
