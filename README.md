# 🌼Image Classification of Flowers using Convolutional Neural Network (CNN)
> Deployed to Hugging Face Spaces using a Gradio front-end

<img src="https://github.com/adstika20/flower-deep-classifier/blob/main/assets/kristine-cinate-krlsGrxLa3U-unsplash.jpg?raw=true" width="950"/>


## Pendahuluan Proyek

Deep Learning adalah salah satu cabang dari Machine Learning yang meniru cara kerja otak manusia dalam mengenali pola dan mempelajari data secara mendalam. Model-model deep learning saat ini banyak digunakan dalam berbagai bidang seperti pengenalan gambar, suara, teks, dan lain-lain.

Proyek ini dibuat sebagai studi kasus sederhana untuk memahami konsep dasar deep learning melalui klasifikasi gambar bunga. Model dilatih untuk mengenali dua jenis bunga, yaitu **dandelion** dan **daisy**, dengan menggunakan arsitektur **Convolutional Neural Network (CNN)**.

Melalui proyek ini, diharapkan pengguna dapat memperoleh pemahaman dasar tentang bagaimana model CNN bekerja, mulai dari proses pelatihan, evaluasi, hingga deployment ke aplikasi berbasis web menggunakan **Gradio** di **Hugging Face**.

## Struktur Repositori
Repositori ini dibangung dengan serangkaian struktur di bawah ini:

```
flower-deep-classifier/
├── app/ # File aplikasi Gradio
│ └── app.py
├── notebooks/ # Notebook eksplorasi dan pelatihan model
│ ├── 01_data_exploration.ipynb
│ └── 02_model_training.ipynb
├── save_model/ # Model hasil training (README + link drive)
│ └── README.md
├── assets/ # Gambar untuk dokumentasi
│ └── kristine-cinate-*.jpg
├── requirements.txt
└── README.md

```

## Cara Menjalankan Proyek


#### Clone repositori
``````bash
git clone https://github.com/adstika20/flower-deep-classifier.git
cd flower-deep-classifier
pip install -r requirements.txt
python app/app.py

``````


## Dataset
Dataset yang digunakan berasal dari Roboflow dan dapat diakses melalui tautan berikut:

🔗 [Informasi Dataset dan Model](https://github.com/adstika20/flower-deep-classifier/tree/b0efd7b1e73d2f07ae6f8cbaab03c21c3e2191f3/save_model)

Di dalam folder tersebut juga tersedia file model terlatih berformat **HDF5 (.h5)** — yaitu format standar yang digunakan untuk menyimpan arsitektur dan bobot model deep learning di Keras atau TensorFlow.

Silakan kunjungi tautan tersebut untuk:
- Melihat sumber dataset bunga (daisy dan dandelion)
- Mengunduh file model yang sudah dilatih
- Mengetahui cara memuat model kembali di Google Colab


## Model Deep Learning
Convolutional Neural Network (CNN)


## Hasil dan Analisis
1. Training Progres
   ![Training Progres Overview](https://github.com/adstika20/flower-deep-classifier/blob/main/assets/Training%20Progress%20Overview.png)
   
3. Confussion Matriks

![Confusion Matriks](https://github.com/adstika20/flower-deep-classifier/blob/main/assets/Confusion%20Matrix.png)

3. Kesalahan Prediksi
   
![Kesalahan prediksi](https://github.com/adstika20/flower-deep-classifier/blob/main/assets/Jumlah%20gambar%20yang%20salah%20diprediksi.png)
   
## Penutup
