import pandas as pd
from textblob import TextBlob

def load_data(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna(subset=['price', 'name'])
    return df

def analyze_title_sentiment(text):
    analysis = TextBlob(str(text))
    if analysis.sentiment.polarity > 0:
        return 'Positif (Menarik)'
    elif analysis.sentiment.polarity < 0:
        return 'Negatif/Kurang Menarik'
    else:
        return 'Netral'

def process_airbnb_data(df):
    # Ambil sampel 2000 baris agar aplikasi Streamlit ringan dan cepat
    if len(df) > 2000:
        df = df.sample(n=2000, random_state=42)
    df['Title_Sentiment'] = df['name'].apply(analyze_title_sentiment)
    return df