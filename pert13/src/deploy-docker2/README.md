# Deployment Model Prediksi IPK

## Deskripsi singkat

Repository ini berisi semua file yang dibutuhkan untuk melakukan deployment model Prediksi IPK. Adapun model yang digunakan merupakan model untuk memprediksi nilai IPK berdasarkan nilai raport mata pelajaran:

- Bahasa Indonesia
- Bahasa Inggris
- Matematika

Prediksi dilakukan hanya berdasarkan tiga mata pelajaran tersebut karena hanya ketiga mata pelajaran itu yang diajarkan di __semua__ jenis sekolah (baik SMA, SMK, maupun MA).

## Sekilas mengenai input model

Agar dapat memprediksi nilai IPK, data input model harus mengikuti format sebagai berikut:\
`[Bahasa_Indonesia, Matematika, Bahasa_Inggris]`

Sebagai contoh\
Bahasa Indonesia: 75\
Matematika: 80\
Bahasa Inggris: 84

Akan diubah menjadi:\
`[75, 80, 84]`

## Folder, file, dan kegunaannya

-   templates/
-   index.html --> Berisi template website
-   app.py --> Berisi konfigurasi route untuk API
-   model.joblib --> Model Regresi Linier yang sudah di-training
-   requirements.txt --> Berisi daftar dependency/package Python yang diperlukan untuk menjalankan API dan model Regresi Linier

## Cara menjalankan API pada komputer Anda

### Menjalankan API

1. Pastikan Anda sudah menginstall Anaconda
1. Buka terminal/command prompt/power shell
1. Buat virtual environment dengan\
   `conda create -n <nama-environment> python=3.9`
1. Aktifkan virtual environment dengan\
   `conda activate <nama-environment>`
1. Install semua dependency/package Python dengan\
   `pip install -r requirements.txt`
1. Jalankan API menggunakan perintah\
   `python app.py`

### Akses melalui Website

Setelah API berjalan:

1. Anda akan diberikan URL untuk membuka website berupa `localhost:5000/` atau `127.0.0.1:5000/`
1. Buka URL dengan browser, coba masukkan data yang ingin di prediksi
1. Anda akan diberikan hasil estimasi nilai IPK
