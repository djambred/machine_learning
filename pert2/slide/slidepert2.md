---
marp: true
theme: uncover
paginate: false
size: 4:3
---
<style>
    :root {
        --color-background: #101010;
        --color-foreground: #FFFFFF;
        font-family: MesloLGS NF;
        font-size : 20px;
    }
    h1 {
        font-size : 40px;
    }

    header {
        top: 30px;
    }

    code.python {
        background: lightyellow;
    } 

    footer {
        bottom: 30px;
    }
    
</style>
![bg contain opacity blur](ueu.png)
# Pengantar Pemograman Python
### oleh
#### 8126 - Jefry Sunupurwa Asri S.Kom., M.Kom

---
![bg contain opacity blur](ueu.png)
# Mengapa Python?
- Bahasa pemograman tingkat tinggi
- Penulisan kode/sintaks lebih sederhana dan tersedia banyak library
- Bersifat open-source dan cross-platform
- Biasa digunakan oleh
    - data analyst
    - data engineer
    - data scientist
    - business intelligence
    - machine learning engineer
- Cocok untuk pemula
- Sederhana tapi powerfull

---
![bg contain opacity blur](ueu.png)
# Keunggulan Python
- Readibility, python mudah dibaca dan dipahami
- Efisien, memiliki library yang lengkap sehingga penulisan coding dapat lebih sederhana
- Multifungsi, dengan menggunakan python dapat membuat website, aplikasi bidang robotika dan aplikasi bidang kecerdasan buatan (AI)
- Interoperabilitas, python mampu berinteraksi dengan bahasa pemograman lainnya
- Dukungan komunitas, python merupakan program open-source dan komunitas python sangat aktif dalam melakukan pengembangan

---
![bg contain opacity blur](ueu.png)
# Penerapan Python pada Project
- Data Exploration
    - scraping, crawling, data mining
    - coding, query
- Data Preprocessing
    - seleksi fitur, statistika deskriptif, class balancing, visualisasi data
    - transformasi fitur: categorical encoding, binning
- Data Cleansing
    - Menangani nilai kosong (missing values), menghapus baris terduplikasi
    - Data formating, menangani data pencilan (outliers)
- Data Modeling
    - melatih data dengan algoritma Machine Learning
    - Melakukan klasifikasi, regresi, prediksi atau klasterisasi

---
![bg contain opacity blur](ueu.png)
# Konsep Python (REPL environment)
- **R**ead (Proses membaca code)
- **E**val (Proses evaluasi code)
- **P**rint (Proses menampilkan code)
- **L**oop (Pengulangan Proses R-E-P)
> contoh codingan 
>> ```python
> a = 2 + 3
> print(a)
> ```

---
![bg contain opacity blur](ueu.png)
# Type Data Python
- Integer (bilangan bulat negatif maupun positif)
- Float (bilangan pecahan negatif maupun positif)
- Str (berupa angka, huruf dan simbol)
- Boolean (berupa keluaran true or false)
- Casting (pengubahan tipe data misalnya int to float)
- List (daftar elemen atau array)

---
![bg contain opacity blur](ueu.png)
# Library yang akan sering digunakan
- Numpy (digunakan untuk perhitungan saintifik)
- Scikit-Learn (digunakan untuk mempraktikan machine learning dan membuat model)
- Matplotlib (digunakan untuk visualisasi data dua dimensi)
- Pandas (digunakan untuk data struktur dan data analisis)
- Scipy (digunakan untuk bekerjasama dengan numpy dalam algoritma numerik, optimasi dan statistika)
- Seaborn (digunakan untuk high-level interface statistika informatif)
- Tensorflow (digunakan untuk komputasi machine learning berskala besar)

---
![bg contain opacity blur](ueu.png)
# Pengenalan Git
- Git merupakan kakas yang bersifat open source  untuk memudahkan bekerja dengan proyek  berskala kecil maupun besar
- Git memiliki tiga status utama tempat file berada:
modified, staged, committed:
    - Modified berarti Anda telah mengubah file tetapi belum menyimpannya ke database Anda
    - Staged berarti Anda telah menandai file yang  dimodifikasi dalam versi terbaru untuk masuk ke  tahap commit
    - Commit berarti bahwa data disimpan dengan aman  di database local Anda

>> CONTOH PENGGUNAAN CLI GIT
>>> Inisialisasi: 
>>> git init
>> Commit: 
>>> git commit -m "first commit"  
>>Branch: 
>>> git branch -M main
>> Add Remote: 
git remote add origin https://github.com/[user]/[repo].git
>> Push: 
>>> git push -u origin main  
>>> Pull: 
>>> git pull origin [branch]


