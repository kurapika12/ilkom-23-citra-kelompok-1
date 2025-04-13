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
    
                # Create histogram for greyscale image
                plt.figure()
                plt.hist(img.ravel(), bins=256, range=[0, 256], color='gray')
                plt.title('Histogram Greyscale')
                plt.xlabel('Pixel Value')
                plt.ylabel('Frequency')
                hist_path = os.path.join(STATIC_FOLDER, "histogram_greyscale.png")
                plt.savefig(hist_path)
                plt.close()
                   
                session["histogram_greyscale"] = "histogram_greyscale.png"
            else:
                # Untuk Analisis warna dominan
                total_b = np.sum(img[:,:,0])
                total_g = np.sum(img[:,:,1])
                total_r = np.sum(img[:,:,2])
   
                # Untuk Menghitung persentase
                total_all = total_b + total_g + total_r
                percent_b = (total_b / total_all) * 100
                percent_g = (total_g / total_all) * 100
                percent_r = (total_r / total_all) * 100
   
                # Menentukan warna dominan
                if total_r > total_g and total_r > total_b:
                    dominant_color = "Merah"
                    dominant_percent = percent_r
                elif total_g > total_r and total_g > total_b:
                    dominant_color = "Hijau"
                    dominant_percent = percent_g
                else:
                    dominant_color = "Biru"
                    dominant_percent = percent_b

                dominant_info = {
                    "color": dominant_color,
                    "percent": round(dominant_percent, 2),
                    "blue": round(percent_b, 2),
                    "green": round(percent_g, 2),
                    "red": round(percent_r, 2),
                    "is_greyscale": False
                }
 
                # membuat histogram untuk masing-masing channel warna
                colors = ('b', 'g', 'r')
                channel_names = ('Blue', 'Green', 'Red')
   
                # membuat 3 histogram terpisah
                for i, (col, name) in enumerate(zip(colors, channel_names)):
                    plt.figure()
                    plt.hist(img[:, :, i].ravel(), bins=256, range=[0, 256], color=col)
                    plt.title(f'Histogram Channel {name}')
                    plt.xlabel('Pixel Value')
                    plt.ylabel('Frequency')
                    hist_path = os.path.join(STATIC_FOLDER, f"histogram_{name.lower()}.png")
                    plt.savefig(hist_path)
                    plt.close()
                                    