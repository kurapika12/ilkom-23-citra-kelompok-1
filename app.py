from flask import Flask, request, render_template, send_file, redirect, url_for, session
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import glob

import matplotlib
matplotlib.use("Agg")  #Tambahkan ini untuk menghindari masalah GUI Matplotlib

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

            if len(img.shape) == 2:
                equalized_img = cv2.equalizeHist(img)
            else:
                img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
                img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
                equalized_img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

            result_path = os.path.join(STATIC_FOLDER, "equalized.png")
            cv2.imwrite(result_path, equalized_img)

            plt.figure()
            if len(img.shape) == 2:
                plt.hist(img.ravel(), bins=256, range=[0, 256], label='Original', alpha=0.7, color='black')
                plt.hist(equalized_img.ravel(), bins=256, range=[0, 256], label='Equalized', alpha=0.7, color='red')
            else:
                colors = ('b', 'g', 'r')
                for i, col in enumerate(colors):
                    plt.hist(img[:, :, i].ravel(), bins=256, range=[0, 256], label=f'Original {col.upper()}', alpha=0.5, color=col)
                    plt.hist(equalized_img[:, :, i].ravel(), bins=256, range=[0, 256], label=f'Equalized {col.upper()}', alpha=0.5, linestyle='dashed')
            plt.legend()
            plt.xlabel('Pixel Value')
            plt.ylabel('Frequency')
            plt.title('Histogram Perbandingan')
            hist_path = os.path.join(STATIC_FOLDER, "histogram.png")
            plt.savefig(hist_path)
            plt.close()

            session["original"] = "original.png"
            session["result"] = "equalized.png"
            session["histogram"] = "histogram.png"

            return redirect(url_for("result"))

    return render_template("index.html")

@app.route("/result")
def result():
    return render_template("result.html",
                           original=session.get("original"),
                           result=session.get("result"),
                           histogram=session.get("histogram"))

@app.route("/download")
def download():
    result_path = os.path.join(STATIC_FOLDER, "equalized.png")
    return send_file(result_path, as_attachment=True)

if __name__ == "__main__":
    # clear_static_folder()  --> Ini dihapus agar tidak menghapus gambar setiap restart
    app.run()  # Hapus debug=True untuk menghindari masalah tkinter
