import base64
from io import BytesIO
from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np

app = Flask(__name__)
CORS(app)

# Load YOLOv8 model
model = YOLO("modelbest.pt")

@app.route("/isalive", methods=["GET"])
def is_alive():
    return "OK", 200

@app.route("/predict", methods=["POST"])
def predict():
    # Input berupa JSON dengan key 'image' (base64 string)
    data = request.get_json()
    base64_image = data["instances"][0]["image"][0]

    # Decode base64 menjadi gambar
    img_data = base64.b64decode(base64_image)
    img = Image.open(BytesIO(img_data))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # Jalankan inference dengan YOLOv8
    results = model(img)

    # Proses hasil deteksi
    detections = []
    for r in results:
        for box in r.boxes:
            xyxy = box.xyxy[0].tolist()
            confidence = float(box.conf[0])
            class_id = int(box.cls[0])
            class_name = r.names[class_id]
            detections.append({
                "label": class_name,
                "confidence": confidence,
                "coordinates": xyxy
            })

    return jsonify({"predictions": detections})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
