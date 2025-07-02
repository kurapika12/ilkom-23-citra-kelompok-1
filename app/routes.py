from flask import Blueprint, render_template, request, redirect, url_for, session
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from .utils import clear_static_folder, is_greyscale

main = Blueprint("main", __name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
STATIC_FOLDER = os.path.join(os.path.dirname(__file__), 'static')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

@main.route("/", methods=["GET", "POST"])
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
                total_b = np.sum(img[:, :, 0])
                total_g = np.sum(img[:, :, 1])
                total_r = np.sum(img[:, :, 2])
                total_all = total_b + total_g + total_r
                percent_b = (total_b / total_all) * 100
                percent_g = (total_g / total_all) * 100
                percent_r = (total_r / total_all) * 100

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

                colors = ('b', 'g', 'r')
                channel_names = ('Blue', 'Green', 'Red')

                for i, (col, name) in enumerate(zip(colors, channel_names)):
                    plt.figure()
                    plt.hist(img[:, :, i].ravel(), bins=256, range=[0, 256], color=col)
                    plt.title(f'Histogram Channel {name}')
                    plt.xlabel('Pixel Value')
                    plt.ylabel('Frequency')
                    hist_path = os.path.join(STATIC_FOLDER, f"histogram_{name.lower()}.png")
                    plt.savefig(hist_path)
                    plt.close()

                session["histogram_blue"] = "histogram_blue.png"
                session["histogram_green"] = "histogram_green.png"
                session["histogram_red"] = "histogram_red.png"

            session["original"] = "original.png"
            session["dominant_info"] = dominant_info

            return redirect(url_for("main.result"))

    return render_template("index.html")

@main.route("/result")
def result():
    return render_template("result.html",
                           original=session.get("original"),
                           histogram_blue=session.get("histogram_blue", None),
                           histogram_green=session.get("histogram_green", None),
                           histogram_red=session.get("histogram_red", None),
                           histogram_greyscale=session.get("histogram_greyscale", None),
                           dominant_info=session.get("dominant_info", {}))
