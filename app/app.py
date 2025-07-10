import tensorflow as tf
import numpy as np
import gradio as gr
from PIL import Image

# Load model
model = tf.keras.models.load_model("model.h5")

# Ukuran input
IMG_SIZE = (150, 150)

# Label kelas
class_names = ["Daisy", "Dandelion"]

def predict(image):
    image = image.resize(IMG_SIZE)
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)[0]
    result = {class_names[i]: float(predictions[i]) for i in range(len(class_names))}
    return result

# Gradio UI dengan tema dan styling
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil", label="🌼 Upload Gambar Bunga"),
    outputs=gr.Label(num_top_classes=2, label="📊 Hasil Prediksi"),
    title="🌸 Image Classification of Flowers using Convolutional Neural Network (CNN)",
    description="Klasifikasi gambar bunga menjadi Daisy atau Dandelion 🌼.\n\nGunakan gambar yang jelas agar hasil akurat!",
    theme=gr.themes.Soft(),
    css="""
        body { background-color: #fff8f0; }
        .gr-button { background-color: #ffb6b9; color: #333; font-weight: bold; }
        .gr-input-label, .gr-output-label { color: #4a7c59; font-size: 16px; }
        h1, h2 { color: #4a7c59; }
    """
)

if __name__ == "__main__":
    demo.launch()
