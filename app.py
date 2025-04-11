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

            # Analisis warna dominan
            total_b = np.sum(img[:,:,0])
            total_g = np.sum(img[:,:,1])
            total_r = np.sum(img[:,:,2])
            
            # Hitung persentase
            total_all = total_b + total_g + total_r
            percent_b = (total_b / total_all) * 100
            percent_g = (total_g / total_all) * 100
            percent_r = (total_r / total_all) * 100
            
            # Tentukan warna dominan
            if total_r > total_g and total_r > total_b:
                dominant_color = "Merah"
                dominant_percent = percent_r
            elif total_g > total_r and total_g > total_b:
                dominant_color = "Hijau"
                dominant_percent = percent_g
            else:
                dominant_color = "Biru"
                dominant_percent = percent_b

            # Buat histogram untuk masing-masing channel warna
            colors = ('b', 'g', 'r')
            channel_names = ('Blue', 'Green', 'Red')
            
            