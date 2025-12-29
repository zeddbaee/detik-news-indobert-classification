import streamlit as st
import numpy as np
import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification
import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import os

MODEL_PATH = "rizazaidaan/detiknews-indobert"

LABELS = {
    0: "Finance",
    1: "Food",
    2: "Health",
    3: "Hot",
    4: "Inet",
    5: "News",
    6: "Oto",
    7: "Sport",
    8: "Travel"
}

st.set_page_config(
    page_title="Detik News Classifier",
    layout="centered"
)

st.title("🖥️ Detik News Classifier 🖥️")
st.write("Klasifikasi berita menggunakan model **IndoBERT**.")

@st.cache_resource
def load_model_and_tokenizer():
    print("Sedang memuat model...")
    try:
        tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
        model = TFBertForSequenceClassification.from_pretrained(MODEL_PATH)
        return tokenizer, model
    except Exception as e:
        st.error(f"Gagal memuat model. Pastikan folder '{MODEL_PATH}' berisi file model lengkap.")
        st.error(str(e))
        return None, None


factory_stop = StopWordRemoverFactory()
stopword_remover = factory_stop.create_stop_word_remover()
factory_stem = StemmerFactory()
stemmer = factory_stem.create_stemmer()


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = stopword_remover.remove(text)
    text = stemmer.stem(text)
    return text


with st.spinner("Sedang menyiapkan model AI... (Hanya sekali di awal)"):
    tokenizer, model = load_model_and_tokenizer()

input_text = st.text_area("Masukkan Isi Berita:", height=150, placeholder="Contoh: Harga saham gabungan IHSG hari ini mengalami penurunan drastis...")

if st.button("Analisis Berita", type="primary"):
    if not input_text:
        st.warning("Silakan isi teks berita terlebih dahulu.")
    elif model is None:
        st.error("Model belum dimuat dengan benar.")
    else:
        try:
            # A. Progress
            progress_bar = st.progress(0)
            status_text = st.empty()

            # B. Preprocessing
            status_text.text("Membersihkan teks (Stemming & Stopwords)...")
            cleaned_text = clean_text(input_text)
            progress_bar.progress(30)

            with st.expander("Lihat Teks Hasil Cleaning"):
                st.code(cleaned_text)

            # C. Tokenisasi
            status_text.text("Mengubah teks menjadi angka (Tokenizing)...")
            encoded = tokenizer.encode_plus(
                cleaned_text,
                add_special_tokens=True,
                max_length=100,  # Sesuaikan dengan training
                padding='max_length',
                return_attention_mask=True,
                truncation=True,
                return_tensors='tf'
            )
            input_ids = encoded['input_ids']
            attention_mask = encoded['attention_mask']
            progress_bar.progress(60)

            # D. Prediksi
            status_text.text("Sedang memprediksi...")
            prediction = model.predict([input_ids, attention_mask])
            logits = prediction.logits

            probs = tf.nn.softmax(logits).numpy()[0]
            pred_label_id = np.argmax(probs)
            pred_label_name = LABELS[pred_label_id]
            confidence = probs[pred_label_id] * 100

            progress_bar.progress(100)
            status_text.empty()

            # E. Hasil
            st.success("Analisis Selesai!")

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Kategori Berita", pred_label_name)
            with col2:
                st.metric("Tingkat Keyakinan", f"{confidence:.2f}%")

            st.subheader("Detail Probabilitas:")
            st.bar_chart({LABELS[i]: probs[i] for i in range(len(LABELS))})

        except Exception as e:

            st.error(f"Terjadi kesalahan saat memproses: {e}")

