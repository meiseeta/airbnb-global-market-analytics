#  Global Airbnb Market Insights & Sentiment Dashboard

Aplikasi Dashboard Interaktif berbasis **Streamlit** untuk menganalisis tren harga, sebaran geografis (Geospatial), dan analisis sentimen gaya bahasa pada judul listing Airbnb di berbagai kota besar dunia.

Proyek ini menggabungkan analisis metrik bisnis dengan kemampuan NLP (*Natural Language Processing*) dasar untuk melihat apakah visualisasi bahasa pada judul iklan berpengaruh terhadap harga sewa properti.

---

##  Fitur Utama
- **Geospatial Mapping:** Visualisasi interaktif sebaran properti di peta dunia menggunakan koordinat Latitude & Longitude (via Plotly & OpenStreetMap).
- **Business Financial Metrics:** Menampilkan rata-rata harga, total listing, dan tingkat popularitas berdasarkan jumlah review secara real-time.
- **Dynamic Filtering:** Filter data secara interaktif berdasarkan pilihan Kota dan Tipe Kamar (*Room Type*).
- **NLP Title Sentiment Analysis:** Menggunakan library `TextBlob` untuk mengklasifikasikan gaya bahasa judul iklan properti menjadi *Positif (Menarik)*, *Netral*, atau *Kurang Menarik*, lalu mengorelasikannya dengan harga.

---

##  Tech Stack & Library
- **Bahasa:** Python
- **Dashboard UI:** Streamlit
- **Data Manipulation:** Pandas
- **Interactive Visualization:** Plotly Express
- **Natural Language Processing (NLP):** TextBlob

---

##  Struktur Proyek
```text
airbnb-global-market-analytics/
├── data/
│   └── airbnb_top_cities.csv    # Dataset utama Airbnb (Sampled)
├── src/
│   └── processor.py             # Logika bisnis & pemrosesan data NLP
├── app.py                       # File utama untuk tampilan UI Streamlit
├── requirements.txt             # Daftar library yang digunakan
└── README.md                    # Dokumentasi proyek
