import cv2
import numpy as np
from ultralytics import YOLO

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
model = YOLO("yolov8n.pt")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def predict_on_image(image_stream):
    image = cv2.imdecode(np.asarray(bytearray(image_stream.read()), dtype=np.uint8), cv2.IMREAD_COLOR)

    results = model.predict(image,classes=0 , conf=0.5)
    for i, r in enumerate(results):
        im_bgr = r.plot()

    return im_bgr
