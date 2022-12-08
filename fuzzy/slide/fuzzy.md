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

    code.python {
        background: lightyellow;
    } 

    footer {
        bottom: 30px;
    }
    
</style>
![bg contain opacity blur](ueu.png)
# FUZZY LOGIC
### oleh
#### 8126 - Jefry Sunupurwa Asri S.Kom, M.Kom

---
![bg contain opacity blur](ueu.png)
# Apa itu Fuzzy Logic?
adalah suatu cara yang tepat untuk memetakan suatu ruang input ke dalam suatu ruang output.

---
![bg contain opacity blur](ueu.png)
# Kenapa menggunakan Fuzzy Logic
- Mudah dimengerti
- Sederhana
- Fleksibel
- Memiliki toleransi terhadap data yang tidak tepat
- dapat membangun dan mengaplikasikan pengalaman para pakar
- dapat digabungkan dengan teknik kendali konvensional
---
![bg contain opacity blur](ueu.png)
# Contoh Penerapan Fuzzy
- Transmisi otomatis pada mobil. Mobil Nissan telah menggunakan sistem fuzzy pada transmisi otomatis, dan mampu menghemat bensin 12 – 17%.
- Ilmu kedokteran dan biologi, seperti sistem diagnosis yang didasarkan pada logika  fuzzy,  penelitian  kanker,  manipulasi  peralatan  prostetik  yang didasarkan pada logika fuzzy, dll. 
- Ilmu lingkungan, seperti kendali kualitas air, prediksi cuaca, dll.
- Teknik, seperti perancangan jaringan komputer, prediksi adanya gempa bumi, dll.

---
![bg contain opacity blur](ueu.png)
# Himpunan Fuzzy Logic
Pada himpunan tegas (crisp set), nilai keanggotaan suatu item x dalam suatu himpunan A memiliki 2 kemungkinan :
 * Satu (1), artinya x adalah anggota A
 * Nol (0), artinya x bukan anggota A
```
Contoh :
Jika diketahui :
	S={1,2,3,4,5,6} adalah semesta pembicaraan
	A={1,2,3}
	B={3,4,5}

	maka :
        Nilai keanggotaan 2 pada A, [2] = 1, 
        Nilai keanggotaan 4 pada A, [4] = 0, 
```
```
Contoh :
“Jika suhu lebih tinggi atau sama dengan 80 oF, maka suhu disebut panas, sebaliknya disebut tidak panas”

Kasus :
        Suhu = 100 oF, maka Panas
        Suhu = 80.1 oF, maka Panas
        Suhu = 79.9 oF, maka tidak panas
        Suhu = 50 oF, maka tidak panas
            If Suhu ≥ 80 oF, disebut panas
            If Suhu < 80 oF, disebut tidak panas

Fungsi keanggotaan dari himpunan tegas gagal membedakan antara anggota pada himpunan yang sama
Ada problem-problem yang terlalu kompleks untuk didefinisikan secara tepat
```

---
![bg contain opacity blur](ueu.png)
CONTOH IMPLEMENTASI ADA DI GITHUB

---
![bg contain opacity blur](ueu.png)
# ADA PERTANYAAN?

---
![bg contain opacity blur](ueu.png)
# TERIMA KASIH