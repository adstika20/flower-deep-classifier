
---

## 🚀 Cara Buat `README.md` Ini dari Colab

```python
readme_text = """# Folder Save Model

Model `.h5` tidak disimpan langsung di dalam repository ini karena ukurannya besar dan GitHub membatasi ukuran file maksimal 100 MB.

Sebagai gantinya, model dapat dimuat dari Google Drive dengan perintah berikut di Google Colab:

```python
from google.colab import drive
drive.mount('/content/drive')

from tensorflow.keras.models import load_model
model = load_model("/content/drive/MyDrive/My Models/model.h5")
