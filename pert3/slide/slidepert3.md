---
marp: true
theme: uncover
paginate: false
size: 4:3
---
<style>
    :root {
        --color-background: #FFFFFF;
        --color-foreground: #101010;
        font-family: MesloLGS NF;
        font-size : 20px;
    }
    h1 {
        font-size : 40px;
    }

    header {
        top: 30px;
    }

    footer {
        bottom: 30px;
    }
    
</style>
![bg contain opacity blur](ueu.png)
# Business Understanding
### oleh
#### 8126 - Jefry Sunupurwa Asri S.Kom., M.Kom

--- 
![bg contain opacity blur](ueu.png)
# Apa itu Business Understanding
- Tahap 1 : Identifying Business Goal
Hal pertama yang harus Anda lakukan dalam proyek apa pun adalah mencari tahu persis apa yang ingin di capai
- Tahap 2 : Assesing Situation
Masuk ke detail lebih lanjut tentang masalah yang terkait dengan tujuan bisnis
- Tahap 3 : Producing Project Plan
Tentukan setiap langkah dalam penyelesaian masalah dalam mencapai tujuan tersebut dan tinjau ulang hasilnya

---
![bg contain opacity blur](ueu.png)
![image](ScopeBU.png)

---
![bg contain opacity blur](ueu.png)
# Businees Background
### Tahap 1 — Menentukan Struktur Organisasi
- Kembangkan bagan organisasi untuk menggambarkan divisi perusahaan, departemen, dan grup proyek 
- Mengidentifikasi individu kunci dalam organisasi.
- Identifikasi unit bisnis yang akan terpengaruh oleh proyek data mining.
### Tahap 2 — Menjelaskan Area Masalah
- Identifikasi area masalah, seperti pemasaran, layanan pelanggan, atau pengembangan bisnis.
- Jelaskan masalah secara umum.
### Tahap 3 — Jelaskan Solusi Saat Ini
- Jelaskan solusi apa pun yang saat ini digunakan untuk mengatasi masalah bisnis.
- Jelaskan keuntungan dan kerugian dari solusi saat ini. Juga, atasi tingkat penerimaan yang dimiliki solusi ini dalam organisasi.

---
![bg contain opacity blur](ueu.png)
# Businees Goals
**Setelah mendapatkan background bisnis kita dapat memetakan**
- Tujuan bisnis
    - Kendala (keterbatasan apa yang dapat Anda lakukan, jenis solusi yang dapat digunakan, kapan pekerjaan harus diselesaikan, dan sebagainya)
    - Dampak (bagaimana masalah dan solusi yang mungkin cocok dengan bisnis)
- Latar Belakang: Menjelaskan situasi bisnis yang mendorong proyek. Item ini, seperti banyak item berikutnya, hanya berjumlah beberapa paragraf.
- Tujuan bisnis: Tentukan apa yang ingin dicapai dengan proyek tersebut. Misalnya, sasaran bisnis mungkin adalah meningkatkan penjualan dari sebesar 10 persen dari tahun ke tahun.
- Kriteria keberhasilan bisnis: Tentukan bagaimana hasil akan diukur. Cobalah untuk mendapatkan kriteria keberhasilan kuantitatif yang jelas. Jika Anda harus menggunakan kriteria subjektif setidaknya dapatkan kesepakatan tentang siapa yang akan menilai apakah kriteria tersebut telah terpenuhi atau tidak.

---
![bg contain opacity blur](ueu.png)
# Businees Success Criteria
- SUBJECTIVE
Kriteria ini lebih sulit untuk dijabarkan, tetapi kita dapat menyepakati siapa yang membuat keputusan akhir
- OBJECTIVE
Kriteria ini bisa sesederhana peningkatan spesifik dalam akurasi audit

---
![bg contain opacity blur](ueu.png)
# Assessing your situation
- Inventory of Resource
Daftar semua sumber daya yang tersedia untuk proyek, termasuk data, perangkat keras, dan perangkat lunak.
- Requirement, Assumption and Constraints
Persyaratan akan mencakup jadwal penyelesaian, kewajiban hukum dan keamanan, dan persyaratan untuk pekerjaan akhir yang dapat diterima.
- Risk and Contingencies
Identifikasi penyebab yang dapat menunda penyelesaian proyek, dan siapkan rencana backup untuk masing-masing penyebab tersebut
- Terminology
Buat daftar istilah bisnis dan istilah penambangan data yang relevan dengan proyek Anda dan tuliskan dalam glosarium dengan definisi (dan mungkin contoh), sehingga semua orang yang terlibat dalam proyek dapat memiliki pemahaman yang sama tentang istilah tersebut.
- Costs and Benefit
Siapkan analisis biaya-manfaat untuk proyek

---
![bg contain opacity blur](ueu.png)
# Producing Project Plan
Buat garis besar rencana tindakan langkah demi langkah untuk proyek tersebut. Perluas kerangka dengan jadwal penyelesaian setiap langkah, sumber daya yang diperlukan, input (seperti data atau pertemuan dengan pakar materi pelajaran), dan output (seperti data yang dibersihkan, model, atau laporan) untuk setiap langkah, dan dependensi (langkah-langkah yang tidak dapat dimulai sampai langkah ini selesai). Nyatakan secara eksplisit bahwa langkah-langkah tertentu harus diulang (misalnya, pemodelan dan evaluasi biasanya memerlukan beberapa pengulangan bolak-balik).

---
![bg contain opacity blur](ueu.png)
# Data Collection
Pada tahap pengumpulan data awal dapat melakukan identifkasi data tersebut dengan 3 bentuk yakni terstruktur, tidak terstruktur dan semi-terstruktur.

# Gathering Data
Data dapat dikumpulkan dari beberapa sumber yakni internal (excel, database, dll), Web Scraping atau API, Data Public dan Open Data


---
![bg contain opacity blur](ueu.png)
# DATA PREPROCESSING
Data preprocessing merupakan sekumpulan teknik yang diterapkan pada database untuk menghapus noise, missing value, dan data yang tidak konsisten. Data preprocessing dibagi menjadi beberapa langkah, yaitu cleaning data, data transformation, dan data reduction. Data preprocessing ini digunakan karena dalam data realtime database seringkali tidak lengkap dan tidak konsisten sehingga mengakibatkan hasil data mining tidak tepat dan kurang akurat. Oleh karena itu, untuk meningkatkan kualitas data yang akan dianalisis, perlu dilakukan langkah-langkah preprocessing data. Langkah-langkah tersebut tidak harus semuanya dilakukan. 

---
![bg contain opacity blur](ueu.png)
# Data Cleaning
Data yang baru saja dikumpulkan kemungkinan besar memiliki banyak bagian yang tidak relevan bahkan ada bagian yang hilang. Oleh karena itu perlu adanya proses pembersihan data atau biasa dikenal dengan data cleaning. Hal yang bisa diatasi menggunakan data cleaning adalah penanganan missing value dan noise. Missing value merupakan kondisi dimana adanya data yang hilang atau tidak lengkap di dalam database.

---
![bg contain opacity blur](ueu.png)
# Data Transformation
Data transformation digunakan untuk mengubah data dalam bentuk yang sesuai dalam proses data mining. Beberapa teknik untuk data transformation adalah normalization, pemilihan attribute, dan discretization. Normalization dilakukan untuk menskalakan nilai data dalam rentang nilai tertentu, misalnya -1 sampai 1 atau 0 sampai 1. Teknik kedua adalah pemilihan atribut. Pemilihan atribute merupakan proses pemilihan atribut yang diberikan untuk proses data mining. Terakhir adalah teknik discretization. Teknik ini dilakukan untuk mengganti raw value pada atribut numerik dengan nilai interval.

---
![bg contain opacity blur](ueu.png)
# Data Reduction
Analisis data yang menggunakan dataset dalam ukuran besar akan sangat sulit dilakukan, oleh karena itu, perlu adanya teknik data reduction dengan tujuan untuk meningkatkan efisiensi penyimpanan serta mengurangi biaya penyimpanan dan analisis data. Data reduction dibagi menjadi beberapa teknik, yaitu Data Cube Aggregation, Attribute Subset Selection, Numerosity Reduction, dan Dimensionality Reduction. Teknik-teknik ini memiliki fungsi dan tujuan masing-masing.

---
![bg contain opacity blur](ueu.png)
# Terima Kasih