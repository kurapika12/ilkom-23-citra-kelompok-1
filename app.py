from flask import Flask, request, render_template, send_file, redirect, url_for, session
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import glob

import matplotlib
matplotlib.use("Agg")  # Untuk menghindari masalah GUI Matplotlib

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = "uploads"
STATIC_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

def clear_static_folder():
    files = glob.glob(os.path.join(STATIC_FOLDER, "*"))
    for f in files:
        os.remove(f)

def is_greyscale(img):
    # Check if image is greyscale by comparing color channels
    if len(img.shape) < 3:
        return True
    if img.shape[2] == 1:
        return True
    b, g, r = img[:,:,0], img[:,:,1], img[:,:,2]
    # If all channels are equal, it's greyscale
    if np.allclose(b, g) and np.allclose(b, r):
        return True
    return False

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        clear_static_folder()
        file = request.files["image"]
        if file:
            filename = file.filename
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            img = cv2.imread(filepath)
            original_path = os.path.join(STATIC_FOLDER, "original.png")
            cv2.imwrite(original_path, img)

            # Check if image is greyscale
            greyscale = is_greyscale(img)
  
            if greyscale:
                dominant_info = {
                    "color": "Greyscale",
                    "percent": 100,
                    "blue": 0,
                    "green": 0,
                    "red": 0,
                    "is_greyscale": True
                }
                       