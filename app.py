import streamlit as st
import plotly.express as px
from src.processor import load_data, process_airbnb_data

st.set_page_config(page_title="Airbnb Global Insights", layout="wide")

st.title(" Global Airbnb Market Insights Dashboard")
st.write("Analisis tren harga, lokasi, dan sentimen judul properti di berbagai kota dunia.")

try:
    raw_df = load_data("data/airbnb_top_cities.csv")
    df = process_airbnb_data(raw_df)
    
    # FILTER SIDEBAR
    st.sidebar.header("Filter Data")
    available_cities = df['city'].unique()
    selected_city = st.sidebar.selectbox("Pilih Kota:", available_cities)
    
    room_types = df['room_type'].unique()
    selected_rooms = st.sidebar.multiselect("Tipe Kamar:", room_types, default=room_types)
    
    filtered_df = df[(df['city'] == selected_city) & (df['room_type'].isin(selected_rooms))]
    
    # KARTU METRIK UTAMA
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Listing Ditampilkan", len(filtered_df))
    col2.metric("Rata-rata Harga", f"${filtered_df['price'].mean():.2f}")
    col3.metric("Rata-rata Jumlah Review", f"{filtered_df['number_of_reviews'].mean():.1f}")
    
    st.markdown("---")
    
    # PETA DAN GRAFIK HARGA
    left_col, right_col = st.columns(2)
    
    with left_col:
        st.subheader(f" Peta Sebaran Properti di {selected_city}")
        fig_map = px.scatter_mapbox(
            filtered_df, lat="latitude", lon="longitude", 
            color="room_type", size="price",
            hover_name="name", hover_data=["price", "number_of_reviews"],
            zoom=10, height=400
        )
        fig_map.update_layout(mapbox_style="open-street-map", margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig_map, use_container_width=True)
        
    with right_col:
        st.subheader(" Distribusi Harga Berdasarkan Tipe Kamar")
        fig_box = px.box(filtered_df, x="room_type", y="price", color="room_type")
        st.plotly_chart(fig_box, use_container_width=True)
        
    st.markdown("---")
    
    # ANALISIS SENTIMEN JUDUL
    st.subheader(" Analisis Sentimen Judul Properti")
    sentiment_col, price_analysis_col = st.columns(2)
    
    with sentiment_col:
        fig_pie = px.pie(filtered_df, names='Title_Sentiment', title="Proporsi Gaya Bahasa Judul")
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with price_analysis_col:
        avg_price_sentiment = filtered_df.groupby('Title_Sentiment')['price'].mean().reset_index()
        fig_bar = px.bar(avg_price_sentiment, x='Title_Sentiment', y='price', color='Title_Sentiment', title="Rata-rata Harga vs Sentimen Judul")
        st.plotly_chart(fig_bar, use_container_width=True)

except FileNotFoundError:
    st.error("File 'airbnb_top_cities.csv' tidak ditemukan di folder 'data/'. Pastikan letak dan nama filenya benar!")