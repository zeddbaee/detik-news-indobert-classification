# 🖥️ Detik News Classifier

Aplikasi web untuk mengklasifikasikan berita menggunakan model **IndoBERT**. Aplikasi ini dapat mengkategorikan berita ke dalam 9 kategori: Finance, Food, Health, Hot, Inet, News, Oto, Sport, dan Travel.

---

## 🌐 Akses Aplikasi

Aplikasi sudah di-deploy dan dapat diakses langsung di:

### 👉 **[https://detiknews-indobert.streamlit.app/](https://detiknews-indobert.streamlit.app/)**

---

## 📋 Daftar Isi

- [Akses Aplikasi](#-akses-aplikasi)
- [Fitur](#-fitur)
- [Cara Penggunaan](#-cara-penggunaan)
- [Label Kategori](#-label-kategori)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)

---

## ✨ Fitur

- 🤖 Klasifikasi berita otomatis menggunakan IndoBERT
- 📝 Preprocessing teks (cleaning, stemming, stopword removal)
- 📊 Menampilkan tingkat keyakinan prediksi
- 💻 Antarmuka web yang user-friendly dengan Streamlit

---

## 📖 Cara Penggunaan

1. **Buka aplikasi** di [https://detiknews-indobert.streamlit.app/](https://detiknews-indobert.streamlit.app/)
2. **Tunggu** sebentar hingga model selesai dimuat (hanya di awal)
3. **Masukkan teks berita** pada kolom yang disediakan
4. **Klik tombol "Analisis Berita"**
5. **Tunggu proses** - Aplikasi akan:
   - Membersihkan teks (stemming & stopwords)
   - Mengubah teks menjadi token
   - Memprediksi kategori
6. **Lihat hasil** berupa kategori berita dan tingkat keyakinan

> 💡 **Tips:** Jika aplikasi sedang dalam mode sleep, tunggu beberapa saat hingga server aktif kembali.

---

## 🏷️ Label Kategori

Aplikasi dapat mengklasifikasikan berita ke dalam 9 kategori berikut:

| ID | Kategori | Deskripsi |
|----|----------|-----------|
| 0 | **Finance** | Berita ekonomi & keuangan |
| 1 | **Food** | Berita kuliner & makanan |
| 2 | **Health** | Berita kesehatan |
| 3 | **Hot** | Berita viral & trending |
| 4 | **Inet** | Berita teknologi & internet |
| 5 | **News** | Berita umum |
| 6 | **Oto** | Berita otomotif |
| 7 | **Sport** | Berita olahraga |
| 8 | **Travel** | Berita wisata & perjalanan |

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Keterangan |
|-----------|------------|
| [Streamlit](https://streamlit.io/) | Framework untuk membangun web app |
| [TensorFlow](https://www.tensorflow.org/) | Library deep learning |
| [Transformers](https://huggingface.co/transformers/) | Library untuk model IndoBERT |
| [Sastrawi](https://github.com/har07/PySastrawi) | Library NLP Bahasa Indonesia |
| [NumPy](https://numpy.org/) | Komputasi numerik |

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan akademis (Project Final ML - Semester 5).

---

## 👨‍💻 Dibuat Oleh

**Muhammad Riza Zaidaan**  
Sains Data FATISDA UNS