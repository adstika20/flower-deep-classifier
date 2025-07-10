# 📚Folder Save Model

Folder ini digunakan untuk dokumentasi pemuatan dan penyimpanan model `.h5` dari luar GitHub.

## Asal Usul Model

Model ini merupakan hasil pelatihan (training) image classification menggunakan dataset bunga yang tersedia di Roboflow. Dataset bersifat **public domain** dan diambil dari: [public.roboflow.com](https://public.roboflow.com/classification/flowers_classification)

## Informasi Singkat

- 📊 Total gambar: ~1.821
- 🏷️ Jenis anotasi: Klasifikasi Gambar (Single-Label)  
- 📁 Format: Folder per kelas (klasik image classification)
- 🧪 Cocok untuk: Pelatihan CNN, klasifikasi bunga, eksperimen model ringan

## Cara Memuat Model dari Google Drive

Karena ukuran file `.h5` melebihi batas GitHub (100 MB), file tidak disertakan langsung di repositori ini.

Untuk memuat model di Google Colab, gunakan perintah berikut:

```python
from google.colab import drive
drive.mount('/content/drive')

from tensorflow.keras.models import load_model
model = load_model("/content/drive/MyDrive/My Models/model.h5")

