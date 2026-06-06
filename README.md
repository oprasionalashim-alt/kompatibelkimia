# CHECKCOMCHEMISTRY - Sistem Manajemen Keamanan Bahan Kimia

Aplikasi Streamlit untuk analisis kompatibilitas bahan kimia, visualisasi GHS, dan manajemen database bahan kimia dengan 500+ item.

## 🎯 Fitur Utama

✅ **Cek Kompatibilitas Real-time**
- Analisis kompatibilitas antara 500+ bahan kimia
- Status: AMAN, PERLU PERHATIAN, atau BERBAHAYA
- Penjelasan detail dan rekomendasi penyimpanan

✅ **Dashboard Analytics**
- Visualisasi data dengan grafik Plotly
- Statistik analisis (Total, Aman, Berbahaya, Perlu Perhatian)
- Export data ke CSV/JSON

✅ **Sistem Favorit Lengkap**
- Simpan hasil analisis dengan detail lengkap
- Filter & sort favorit (Terbaru, Terlama, Nama A-Z)
- View detail penjelasan dan rekomendasi
- Export favorit ke JSON
- Cegah duplikasi otomatis

✅ **Database Bahan Kimia**
- 500+ bahan kimia dengan kategori FCOT
- Search & filter berdasarkan kategori
- Sort A-Z atau berdasarkan kategori

✅ **Panduan Interaktif**
- Panduan FCOT (Flammable, Corrosive, Oxidizer, Toxic)
- Panduan GHS (Globally Harmonized System)
- Tips penyimpanan bahan kimia
- FAQ Umum

✅ **Pengaturan & Export**
- Export semua data (history + favorites)
- Hapus data lokal
- Informasi aplikasi lengkap

## 🚀 Cara Menjalankan

### 1. Install Python
- Download dari: https://www.python.org/downloads/
- Pastikan "Add Python to PATH" di-cek saat instalasi

### 2. Clone Repository
```bash
git clone https://github.com/oprasionalashim-alt/kompatibelkimia.git
cd kompatibelkimia
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser pada `http://localhost:8501`

## 📁 Struktur File

```
kompatibelkimia/
├── app.py              # Main application file
├── database.py         # Chemical database & helper functions
├── analyzer.py         # Compatibility analysis functions
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## 🧪 Database Bahan Kimia

Database mencakup bahan kimia dalam 4 kategori utama FCOT:

### 🔥 Flammable (Mudah Terbakar)
- Etanol, Metanol, Acetone, Benzene, Toluene, Xylene, dll.

### 🧪 Corrosive (Korosif)
- HCl, H2SO4, NaOH, KOH, HF, Ammonia Solution, dll.

### ⚡ Oxidizer (Pengoksidasi)
- KMnO4, KNO3, H2O2, NaNO3, Sodium Chlorite, dll.

### ☠️ Toxic (Beracun)
- Mercury, Lead, Arsenic, Cyanide, Formaldehyde, dll.

## 🔄 Sistem Kompatibilitas

### ✅ AMAN - Kombinasi Aman
- Flammable + Flammable
- Corrosive + Corrosive
- Oxidizer + Oxidizer
- Toxic + Toxic
- Dan kombinasi lintas kategori yang aman

### ⚠️ PERLU PERHATIAN - Perlu Monitoring
- Flammable + Corrosive
- Corrosive + Flammable

### ❌ BERBAHAYA - Harus Dipisahkan
- Flammable + Oxidizer (SANGAT BERBAHAYA)
- Corrosive + Oxidizer (SANGAT BERBAHAYA)

## 💾 Fitur Penyimpanan Data

Semua data tersimpan **lokal di browser** menggunakan Streamlit Session State:

### History
- Riwayat semua analisis
- Timestamp otomatis
- Export ke CSV/JSON

### Favorites
- Simpan hasil analisis favorit
- Dengan penjelasan & rekomendasi lengkap
- Filter status (Aman/Berbahaya/Perhatian)
- Sort berbagai cara
- Export individual favorites

## 🎨 UI/UX Features

- Dark theme modern dengan gradient cyan-blue
- Animasi smooth untuk cards dan buttons
- Status color-coded (Green/Red/Orange)
- Responsive design untuk berbagai ukuran layar
- Icon emoji untuk visual clarity

## ⚙️ Teknologi yang Digunakan

- **Streamlit** - Framework web app
- **Pandas** - Data processing
- **Plotly** - Interactive charts
- **Python 3.8+** - Programming language

## 📊 Dashboard Metrics

Dashboard menampilkan:
- Total analisis yang dilakukan
- Jumlah hasil AMAN
- Jumlah hasil BERBAHAYA
- Jumlah hasil PERLU PERHATIAN
- Pie chart distribusi hasil
- Bar chart kategori terpopuler
- Tabel riwayat lengkap

## 🔐 Keamanan Data

- Data tersimpan **hanya di browser lokal**
- Tidak ada data yang dikirim ke server
- Setiap session terpisah
- User dapat menghapus data kapan saja

## 📝 Tips Penggunaan

1. **Cek Kompatibilitas**
   - Pilih dua bahan kimia
   - Klik "Cek Sekarang"
   - Baca penjelasan dan rekomendasi

2. **Simpan Favorit**
   - Setelah analisis, klik "Tambah ke Favorit"
   - Klik tombol mata untuk melihat detail
   - Export untuk arsip

3. **Analisis Dashboard**
   - Lihat trend dan statistik
   - Export data untuk laporan
   - Monitor pola penggunaan

## ⚠️ Disclaimer

**Untuk operasi industri yang sesungguhnya, SELALU konsultasikan dengan ahli keselamatan bahan kimia profesional!**

Aplikasi ini dirancang sebagai alat bantu edukasi dan referensi. Keputusan penyimpanan bahan kimia harus sesuai dengan:
- Standar keselamatan lokal
- Regulasi industri
- Konsultasi expert
- Safety data sheet (SDS) produk

## 👨‍💼 Pengembang

Dibuat oleh: **oprasionalashim-alt**  
Institusi: **Politeknik AKA Bogor**

## 📞 Support

Untuk pertanyaan atau masalah, buka issue di repository ini.

---

**CHECKCOMCHEMISTRY v3.1** - Sistem Manajemen Keamanan Bahan Kimia  
🧪 Keselamatan adalah prioritas utama!
