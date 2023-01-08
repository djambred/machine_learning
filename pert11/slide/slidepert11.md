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
# Dimensionality Reduction
### oleh
#### 8126 - Jefry Sunupurwa Asri S.Kom., M.Kom

---
![bg contain opacity blur](ueu.png)
# Apa itu Dimensinality Reduction?
Dimensionality reduction adalah proses pengurangan dimensi dari data yang berdimensi besar menjadi data yang berdimensi kecil.

---
![bg contain opacity blur](ueu.png)
# Teknik Dalam Dimensionality Reduction
1. Feature Selection 
Feature selection, memilih feature yang berpengaruh dari sekumpulan data asli.
2. Feature Extraction
Feature extraction, membentuk feature baru berdasarkan feature yang lama dengan dimensi yang lebih sedikit dibandingkan dengan sebelumnya.

---
![bg contain opacity blur](ueu.png)
# Algoritma yang biasa digunakan
- PCA (Principal Component Analysis)

- LDA (Linear Discriminant Analysis)


---
![bg contain opacity blur](ueu.png)
# PCA
Merupakan sebuah metode bagaimana mereduksi dimensi dengan menggunakan beberapa garis/bidang yang disebut dengan principle components (PCs). Diharapkan dengan menggunakan beberapa PC, bisa memudahkan kita untuk menginterpretasikan datanya dan melihat pembagian data ke dalam beberapa cluster.
PCA menghasilkan beberapa PCs (principal components), di mana PC1 akan menjelaskan variance terbesar dataset, PC2 menjelaskan variance terbesar setelah PC1, PC3 menjelaskan variance terbesar setelah PC2 dan seterusnya. Masing-masing PC akan membentuk sumbu baru pada visualisasi data.
```
untuk lebih detailnya kita akan mempelajari dengan codingan src/pca/principal_component_analysis.ipynb
```

---
![bg contain opacity blur](ueu.png)
# LDA
Merupakan teknik statistika dalam mereduksi dimensi untuk meingiterpretasikan datanya dan melihat pembagian data ke dalam beberapa cluster.
Menghasilkan beberapa LDs (linear discriminants). LD1 menjelaskan pemisahan (separability) terbesar antar kelompok. LD2 menjelaskan separability terbesar antar kelompok setelah LD1, dan seterusnya. Masing-masing LD akan membentuk sumbu baru pada visualisasi data.
```
untuk lebih detailnya kita akan mempelajari dengan codingan src/lda/linear_discriminant_analysis.ipynb
```

---
![bg contain opacity blur](ueu.png)
# Terima Kasih