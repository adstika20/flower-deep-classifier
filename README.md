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

## Cara Menjalankan Proyek (Secara Lokal)


#### 1. Clone Repository

Buka terminal atau CMD, lalu ketik:

```bash
git clone [https://github.com/username/nama-repo.git](https://github.com/adstika20/flower-deep-classifier.git)
cd flower-deep-classifier
```
#### 2. Buat Virtual Environment (Opsional)
```
python -m venv venv
source venv/bin/activate  # untuk Mac/Linux
venv\Scripts\activate     # untuk Windows
```
#### 3. Install Semua Dependensi
```
pip install -r requirements.txt
```
#### 4. 4. Jalankan Aplikasi
```
python app.py
```
##  Jalankan Online di Hugging Face Spaces (Tanpa Coding)
1. Masuk ke: https://huggingface.co/spaces
2. Klik tombol "Create New Space"
3. Pilih SDK: Gradio, Nama Space: bebas
4. Upload file berikut:
   - app.py
   - model.h5
   - requirements.txt
5. Tunggu proses build selesai, aplikasi siap digunakan online.


## Dataset
Dataset yang digunakan berasal dari Roboflow dan dapat diakses melalui tautan berikut:

🔗 [Informasi Dataset dan Model](https://github.com/adstika20/flower-deep-classifier/tree/b0efd7b1e73d2f07ae6f8cbaab03c21c3e2191f3/save_model)

Di dalam folder tersebut juga tersedia file model terlatih berformat **HDF5 (.h5)** — yaitu format standar yang digunakan untuk menyimpan arsitektur dan bobot model deep learning di Keras atau TensorFlow.

Silakan kunjungi tautan tersebut untuk:
- Melihat sumber dataset bunga (daisy dan dandelion)
- Mengunduh file model yang sudah dilatih
- Mengetahui cara memuat model kembali di Google Colab


## Model Deep Learning
Model Convolutional Neural Network (CNN) ini dirancang untuk melakukan klasifikasi gambar bunga dari dua kategori: Dandelion dan Daisy. Tujuan utamanya untuk secara akurat memprediksi jenis bunga dalam sebuah gambar. Algoritma CNN sangat tepat untuk masalah ini karena kemampuannya yang unggul dalam mengekstrasi fitur spasial hierarkis dari gambar.
Model pada proyek ini akan mengikuti struktur konvensional CNN yang dimulai dengan lapisan konvolusi dan pooling berulang untuk ekstraksi fitur, diikuti oleh lapisan flatten dan fully connected untuk klasifikasi.
```
Input Gambar (150x150x3)
        ↓
[Blok Konvolusi 1: Conv 3x3 (32 Filters), Batch Norm, ReLU, Max Pooling 2x2]
        ↓
[Blok Konvolusi 2: Conv 3x3 (64 Filters), Batch Norm, ReLU, Max Pooling 2x2]
        ↓
[Blok Konvolusi 3: Conv 3x3 (128 Filters), Batch Norm, ReLU, Max Pooling 2x2]
        ↓
[Flatten Layer]
        ↓
[Dropout Layer 0.5]
        ↓
[Fully Connected Layer (128 Neurons), ReLU, L2 Regularization]
        ↓
[Dropout Layer 0.5]
        ↓
[Output Layer (2 Neurons), Softmax]
        ↓
Prediksi Kelas (Dandelion/Daisy)

```

## Hasil dan Analisis
#### 1. Grafik Loss dan Accuracy per Epoch
   
Grafik training progress menunjukkan perkembangan performa model selama proses pelatihan, baik pada data pelatihan (training data) maupun data validasi (validation data).

![ Gambar 1 Training Progres Overview](https://github.com/adstika20/flower-deep-classifier/blob/main/assets/Training%20Progress%20Overview.png)

Grafik bagian kiri menunjukkan bahwa training loss menurun secara stabil, berada di kisaran ~0.77, meskipun terlihat sedikit fluktuatif (zig-zag), yang merupakan hal wajar dalam proses pembelajaran.
Sementara itu, validation loss juga menurun, mencapai sekitar ~0.69, dan trennya stabil.

Grafik bagian kanan memperlihatkan bahwa training accuracy meningkat secara konsisten, dari sekitar 78% hingga mencapai 83%. Sementara itu, validation accuracy memang terlihat lebih fluktuatif, tetapi secara umum menunjukkan tren yang positif, bahkan sempat menyentuh angka akurasi yang lebih tinggi dari training (hingga 89%).

Dengan kata lain, model dalam kondisi stabil, tidak overfit, dan memiliki kemampuan generalisasi yang baik ke data yang belum pernah dilihat sebelumnya.
   
#### 2. Confusion Matrix

Confusion Matrix adalah tabel evaluasi yang menunjukkan jumlah prediksi model yang benar dan salah pada masing-masing kelas, berdasarkan hasil pengujian (test set).

![Confusion Matriks](https://github.com/adstika20/flower-deep-classifier/blob/main/assets/Confusion%20Matrix.png)

Konteks kelas:
```
{'daisy': 0, 'dandelion': 1}
```
Pada bagian baris pertama (Actual = 0), terdapat 117 gambar daisy yang berhasil diprediksi dengan benar sebagai daisy oleh model, dan 12 gambar daisy yang salah diklasifikasikan sebagai dandelion. Sementara itu, pada baris kedua (Actual = 1), tercatat 107 gambar dandelion berhasil diklasifikasikan dengan benar, sedangkan 21 gambar lainnya justru salah ditebak sebagai daisy.

Dengan demikian, confusion matrix ini menggambarkan bahwa model memiliki kemampuan cukup baik dalam membedakan kedua kelas, di mana total prediksi benar (117 + 107) jauh lebih besar dibandingkan total prediksi salah (12 + 21).

Berdasarkan tabel confusion matriks, dapat menghitung statistik evaluasi yang lebih terukur melalui tabel classification report.

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| daisy        | 0.85      | 0.91   | 0.88     | 129     |
| dandelion    | 0.90      | 0.84   | 0.87     | 128     |
| **accuracy** |           |        | 0.87     | 257     |
| macro avg    | 0.87      | 0.87   | 0.87     | 257     |
| weighted avg | 0.87      | 0.87   | 0.87     | 257     |

Precision untuk kelas dandelion sedikit lebih tinggi dibandingkan daisy, namun recall daisy lebih tinggi. Nilai f1-score untuk kedua kelas berkisar antara 0.87 hingga 0.88, menunjukkan bahwa model cukup andal dalam membedakan kedua kelas. Akurasi keseluruhan mencapai 87%, yang berarti model dapat mengklasifikasikan gambar dengan cukup baik. Selain itu, distribusi data antara kedua kelas seimbang, sehingga tidak terjadi bias terhadap salah satu kelas.

#### 3. Kesalahan Prediksi

Berdasarkan confusion matrix, model melakukan 33 kesalahan prediksi: 12 pada kelas daisy dan 21 pada kelas dandelion. Untuk memahami lebih dalam, dilakukan visualisasi atas gambar-gambar yang salah diklasifikasikan. Dengan membandingkan label asli dan hasil prediksi model, kita dapat mengevaluasi pola kesalahan. Visualisasi ini memberikan wawasan tambahan yang tidak bisa dilihat hanya dari angka, dan menjadi alat penting untuk memperbaiki akurasi model di masa depan.
   
![Kesalahan prediksi](https://github.com/adstika20/flower-deep-classifier/blob/main/assets/Jumlah%20gambar%20yang%20salah%20diprediksi.png)
   
## Penutup


