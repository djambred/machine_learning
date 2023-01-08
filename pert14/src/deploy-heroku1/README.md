# Deployment Model ANN (Cat vs Dog)

## Deskripsi singkat

Repository ini berisi semua file yang dibutuhkan untuk melakukan deployment model Machine Learning Image Classification menggunakan ANN (Artificial Neural Network). Adapun model yang digunakan merupakan model untuk memprediksi gambar kucing atau anjing (Cat vs Dog).

#

## Sekilas mengenai input model

Agar dapat memprediksi kucing atau anjing, data input model harus mengikuti format sebagai berikut:

-   Gambar dengan format umum seperti .jpeg, .png, .webp, dsb.
-   Gambar dikonversi ke dalam bentuk array/tensor
-   Nilai pixel gambar memiliki rentang nilai 0-1 dengan cara membagi semua nilai pixelnya dengan 255.0
-   Gambar memiliki dimensi `(1, 256, 256, 3)`

#

## Folder, file, dan kegunaannya

-   static/
    -   uploads/ --> Berisi gambar yang diunggah untuk diprediksi.
-   templates/
    -   index.html --> Berisi template website.
-   app.py --> Berisi konfigurasi route dan proses prediksi model untuk API.
-   model.h5 --> Model Image Classification ANN yang sudah di-training.
-   requirements.txt --> Berisi daftar dependency/package Python yang diperlukan untuk menjalankan API dan model Image Classification ANN.

#

## Cara menjalankan API pada komputer Anda

1. Pastikan Anda sudah menginstall Anaconda.
1. Buka terminal/command prompt/power shell.
1. Buat virtual environment dengan\
   `conda create -n <nama-environment> python=3.9`
1. Aktifkan virtual environment dengan\
   `conda activate <nama-environment>`
1. Install semua dependency/package Python dengan\
   `pip install -r requirements.txt`
1. Jalankan API menggunakan perintah\
   `python app.py`

## Akses melalui Website

1. Anda akan diberikan URL untuk membuka website berupa `localhost:5000/` atau `127.0.0.1:5000/`.
1. Buka URL dengan browser, coba masukkan gambar kucing atau anjing yang ingin di prediksi.
1. Anda akan diberikan prediksi bahwa pada gambar tersebut terdapat kucing atau anjing pada halaman website.
