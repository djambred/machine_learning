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
# Deep Learning
### oleh
#### 8126 - Jefry Sunupurwa Asri S.Kom., M.Kom

---
![bg contain opacity blur](ueu.png)
# Apa itu Deep Learning
Deep Learning adalah seperangkat algoritma dalam machine learning yang berusaha belajar dalam berbagai level sesuai tingkat abstraksi yang berbeda dan terinspirasi dari struktur otak manusia. Struktur tersebut disebut dengan jaringan saraf tiruan (neural network).

---
![bg contain opacity blur](ueu.png)
# Bentuk Arsitektur Deep Learning
![image](deeplearning.png)
Sehingga terdapat 3x4 weight + 4 bias dan 4x2 weight + 2 bias. Total adalah 26 parameter yang pada proses training akan mengalami perubahan untuk mendapatkan hasil yang terbaik.


---
![bg contain opacity blur](ueu.png)
# Penjelasan Arsitektur Deep Learning
Arsitektur diatas biasa disebut Multi Layer Perceptron (MLP) atau Fully-Connected Layer. Dimana Arsitektur pertama memiliki input layer dengan 3 buah neuron pada input layer, dan 2 buah neuron pada output layer. Dan diantara input layer dan output layer terdapat hidden layer. Setiap neuron pada MLP Saling berhubungan ditandai dengan tanda panah. Tiap koneksi memiliki weight yang nantinya nilai dari tiap weight akan berbeda-beda. 

---
![bg contain opacity blur](ueu.png)
# Training Neural Network
Terdapat 2 Tahap
1. Forward Pass
Forward pass atau biasa juga disebut forward propagation adalah proses dimana kita membawa data pada input melewati tiap neuron pada hidden layer sampai kepada output layer yang nanti akan dihitung errornya
![width:750px height:5cm](fwpass.png)
Persamaan diatas adalah contoh forward pass pada arsitektur yang menggunakan ReLU sebagai activation function. Dimana i adalah node pada input layer (3 node input), j adalah node pada hidden layer sedangkan h adalah output dari node pada hidden layer.

---
![bg contain opacity blur](ueu.png)
# Training Neural Network (2)
2. Backward Pass
Error yang kita dapat pada forward pass akan digunakan untuk mengupdate setiap weight dan bias dengan learning rate tertentu.
Kedua proses diatas akan dilakukan berulang-ulang sampai didapatkan nilai weight dan bias yang dapat memberikan nilai error sekecil mungkin pada output layer (pada saat forward pass)

---
![bg contain opacity blur](ueu.png)
# CONTOH PENERAPANNYA 
- src/pendukungslide.ipynb

---
![bg contain opacity blur](ueu.png)
# ALGORITMA YANG BIASA DIGUNAKAN DALAM DEEP LEARNING
- CNN (Convolutional Neural Network)

- RNN (Recurrent Neural Network)

- LSTM (Long Short Term Memory Network)



---
![bg contain opacity blur](ueu.png)
# CNN
CNN terdiri dari banyak layer untuk memproses dan mengekstrak fitur dari data. Ia biasanya digunakan untuk memproses gambar dan mendeteksi objek. Saat ini, CNN banyak digunakan untuk mengidentifikasi citra satelit, citra medis, dan mendeteksi anomali.

---
![bg contain opacity blur](ueu.png)
# RNN
Recurrent Neural Networks (RNN) merupakan salah satu bentuk arsitektur Artificial Neural Networks (ANN) yang dirancang khusus untuk memproses data yang bersambung/ berurutan (sequential data). RNN biasanya digunakan untuk menyelesaikan permasalahan data historis atau time series, contohnya data ramalan cuaca. Selain itu, RNN juga dapat diimplementasikan pada bidang natural language understanding (pemahaman bahasa alami), misalnya  translasi bahasa.

---
![bg contain opacity blur](ueu.png)
# LSTM
LSTM merupakan tipe Recurrent Neural Network yang dapat mempelajari data historis atau time series. Ia merupakan algoritma deep learning yang kompleks dan dapat mempelajari informasi jangka panjang dengan sangat baik. LSTM sangat powerful untuk menyelesaikan berbagai permasalahan kompleks seperti speech recognition, speech to text application, komposisi musik, dan pengembangan di bidang farmasi.

---
![bg contain opacity blur](ueu.png)
# Manfaat Deep Learning

- Dapat memproses unstructured data seperti teks dan gambar.
- Dapat mengotomatisasi proses ekstraksi fitur tanpa perlu melakukan proses pelabelan secara manual.
- Memberikan hasil akhir yang berkualitas.
- Dapat mengurangi biaya operasional.
- Dapat melakukan manipulasi data dengan lebih efektif.

---
![bg contain opacity blur](ueu.png)
# Penerapan Deep Learning
- Pengenalan Gambar
- Pengenalan Suara
- NLP (Natural Language Processing)
- Deteksi Anomali

---
![bg contain opacity blur](ueu.png)
# Terima Kasih