---
marp: true
theme: uncover
paginate: false
size: 4:3
---
<style>
    :root {
        --color-background: #FFFFFF;
        --color-foreground: #000000;
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
# Classification
### oleh
#### 8126 - Jefry Sunupurwa Asri S.Kom., M.Kom


---
![bg contain opacity blur](ueu.png)
# Apa itu Classification?
Secara matematis classification adalah tugas mendekati fungsi pemetaan (f) dari variabel input (X) ke variabel ouput (Y)

---
![bg contain opacity blur](ueu.png)
# Tipe Learner dalam classification
- Lazy Learners
    konsepnya adalah membuat model klasifikasi dengan menunggu data pengujian muncul setelah menyimpan data pelatihan, dan dilakukan setelah mendapat data pengujian. Contohnya : KNN
- Eager Learners
    konsepnya adalah membuat model klasifikasi tanpa menunggu data pengujian muncul setelah data pelatihan. Contohnya : DTC, Naive Bayes

---
![bg contain opacity blur](ueu.png)
# Decision Tree Classification
Secara umum tidak jauh berbeda dengan Decision Tree Regression karena mereka saling terikat dalam penyelesaian, biasanya Classification digunakan untuk menyelesaikan permasalahan Churn Analysis dan Risk Management Sedangkan untuk Regression nya biasa digunakan untuk menyelesaikan permasalahan metode distribusi

---
![bg contain opacity blur](ueu.png)
# K-Nearest Neighbors
![image](knn.png)

---
![bg contain opacity blur](ueu.png)
# Naive Bayes
![image](bayes.png)

---
![bg contain opacity blur](ueu.png)
# Random Forest
![image](rfd.svg)

---
![bg contain opacity blur](ueu.png)
# Support Vector Machine (SVM)
![image](svm.png)
secara sederhana svm mencari hyperplane (batas pemisah) terbaik yang berfungsi sebagai pemisah dua buah class pada input space.


---
![bg contain opacity blur](ueu.png)
# Kernel SVM
![width:500px height:15cm](svmkernel.png)

---
![bg contain opacity blur](ueu.png)
# Terima Kasih