import feedparser
import pandas as pd
import os
from src.utils import random_suffix

rss_sources = {
    "CNN Türk": "https://www.cnnturk.com/feed/rss/all/news",
    "Hürriyet": "https://www.hurriyet.com.tr/rss/gundem",
    "TRT Haber": "https://www.trthaber.com/manset_articles.rss",
    "Sözcü": "https://www.sozcu.com.tr/rss/anasayfa.xml",
    "Habertürk": "https://www.haberturk.com/rss",
    "Yeni Şafak": "https://www.yenisafak.com/rss",
    "Sabah": "https://www.sabah.com.tr/rss/anasayfa.xml",
    "Milliyet": "https://www.milliyet.com.tr/rss/rssNew/gundemRss.xml",
    "Euronews Türkçe": "https://tr.euronews.com/rss?level=theme&name=news",
    "BBC Türkçe": "https://www.bbc.com/turkce/index.xml",
    "Anadolu Ajansı": "https://www.aa.com.tr/tr/rss/default?cat=guncel",
}

def get_haberler(output_dir="data"):
    os.makedirs(output_dir, exist_ok=True)
    random_name = f"haber_gundemi_{random_suffix()}.csv"
    output_file = os.path.join(output_dir, random_name)

    haberler = []
    for name, url in rss_sources.items():
        feed = feedparser.parse(url)
        if feed.entries:
            for entry in feed.entries[:15]:
                haberler.append({
                    "Kaynak": name,
                    "Başlık": entry.title.strip()
                })

    pd.DataFrame(haberler).to_csv(output_file, index=False, encoding="utf-8-sig")
    print(f"✅ Gündem başlıkları '{output_file}' dosyasına kaydedildi.")
    return output_file
