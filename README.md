# Histogram dan Peningkatan Citra (Image Enhancement)

## 📌 Deskripsi Proyek

Proyek ini adalah aplikasi berbasis web yang menggunakan **Flask** dan **OpenCV** untuk menganalisis histogram citra serta meningkatkan kualitas gambar dengan teknik **Histogram Equalization**. Pengguna bisa mengunggah gambar, melihat histogramnya, melakukan enhancement, serta membandingkan gambar sebelum dan sesudah proses.

## 🛠 Teknologi yang Digunakan

- **Python 3**
- **Flask** (Backend)
- **OpenCV** (Pemrosesan citra)
- **HTML dan CSS** (Frontend)
- **Bootstrap** (Styling UI)

## 📂 Struktur Folder

```
/ilkom-23-citra-kelompok-1
│── static/              # Folder untuk file statis (hasil gambar)
│── templates/           # Folder untuk file HTML
│── uploads/             # Folder penyimpanan gambar yang diunggah
│── venv/                # Virtual environment (jangan di-push ke Git)
│── .gitignore           # File untuk mengabaikan file tertentu dalam Git
│── app.py               # Main backend Flask app
│── README.md            # Dokumentasi proyek ini
│── requirements.txt     # Daftar dependensi proyek
```

## 🔧 Cara Instalasi dan Menjalankan

### 1️⃣ **Clone Repo & Masuk ke Direktori**

```bash
git clone https://github.com/kurapika12/ilkom-23-citra-kelompok-1.git
cd ilkom-23-citra-kelompok-1
```

### 2️⃣ **Buat dan Aktifkan Virtual Environment**

#### 💻 **Windows** (Command Prompt / PowerShell)

```bash
python -m venv venv
venv\Scripts\activate
```

#### 🍏 **Mac/Linux** (Terminal)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4️⃣ **Jalankan Aplikasi**

```bash
python app.py
```

Aplikasi akan berjalan di `http://127.0.0.1:5000/`

## ⚙️ Fitur Utama

✅ **Upload Gambar** - Pengguna bisa mengunggah gambar berformat JPG/PNG.<br>
✅ **Tampilkan Histogram** - Histogram gambar asli bisa ditampilkan.<br>
✅ **Histogram Equalization** - Proses peningkatan kualitas gambar dengan teknik equalization.<br>
✅ **Perbandingan Gambar** - Menampilkan sebelum & sesudah enhancement.<br>
✅ **Download Gambar** - Hasil gambar bisa diunduh.

## 📸 Contoh Penggunaan

1. **Upload gambar asli**
2. **Lihat histogram gambar asli**
3. **Klik tombol "Enhance"** untuk menerapkan histogram equalization
4. **Lihat perbandingan gambar sebelum & sesudah**
5. **Download hasil gambar yang telah ditingkatkan**

## 💡 Catatan

- Pastikan gambar dalam format **JPG atau PNG** sebelum diunggah.
- Aplikasi ini hanya mendukung **citra grayscale** untuk histogram equalization.

## ✨ Kontributor

- **M. Aslam Hidayat** - [GitHub Profile](https://github.com/kurapika12)
- **Abdul Mu'iz Azizul Raeba** - [Github Profile](https://github.com/username)
- **Wa Ode Zahra Ramadhani** - [Github Profile](https://github.com/username)
- **Reynaldo Dwi Septano Baru** - [Github Profile](https://github.com/username)
- **Zacky Fiqran Kasmada** - [Github Profile](https://github.com/username)
- **Fitri Nur Ramadhani** - [Github Profile](https://github.com/username)
- **Siti Nur Aisyah Sea** - [Github Profile](https://github.com/username)

---

🚀 Selamat mencoba! Jika ada pertanyaan, silakan ajukan di Issues atau Pull Request. 😃
