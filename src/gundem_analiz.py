import pandas as pd
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer
import re
import os
from src.utils import find_latest_csv, random_suffix

turkish_stopwords = [
    "acaba", "ama", "aslında", "az", "bazı", "belki", "biri", "nın", "nin", "den", "na", "birkaç", "birşey", "biz", "bu", "çok",
    "çünkü", "da", "daha", "de", "defa", "diye", "en", "gibi", "hem", "hep", "hepsi", "her", "hiç",
    "için", "ile", "ise", "kez", "ki", "kim", "mı", "mu", "mü", "nasıl", "ne", "neden", "nerde",
    "nerede", "nereye", "niçin", "niye", "o", "sanki", "şey", "siz", "şu", "tüm", "ve", "veya",
    "ya", "yani", "ben", "sen", "ntv", "yeni", "son", "dakika", "daki", "ka", "oldu", "bölüm", "izle", "onlar",
    "atv", "yayın", "cnn", "kanal", "trend", "ın", "nun", "ün", "dan", "haberi"
]

def analiz_et(haber_file, trend_file, output_dir="data"):
    os.makedirs(output_dir, exist_ok=True)
    random_name = f"analiz_sonuclari_{random_suffix()}.csv"
    output_file = os.path.join(output_dir, random_name)

    if not os.path.exists(haber_file) or not os.path.exists(trend_file):
        raise FileNotFoundError("CSV dosyaları bulunamadı.")

    haber_df = pd.read_csv(haber_file)
    trend_df = pd.read_csv(trend_file).head(100)

    haberler = haber_df["Başlık"].dropna().astype(str).tolist()
    dokumler = trend_df.iloc[:, 0].dropna().astype(str).tolist()
    texts = haberler * 2 + dokumler

    texts = [t for t in texts if re.match(r'^[a-zA-ZçÇğĞıİöÖşŞüÜ0-9\s.,:;!?\'"()\[\]\-–—%]+$', t)]

    embedding_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    vectorizer_model = CountVectorizer(stop_words=turkish_stopwords)

    topic_model = BERTopic(
        language="turkish",
        embedding_model=embedding_model,
        vectorizer_model=vectorizer_model
    )

    topics, probs = topic_model.fit_transform(texts)
    topic_info = topic_model.get_topic_info()
    topic_info.to_csv(output_file, index=False, encoding="utf-8-sig")

    print(f"✅ Analiz tamamlandı: '{output_file}' dosyasına kaydedildi.")
    return output_file
