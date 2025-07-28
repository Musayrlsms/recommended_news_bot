# Recommended_news_bot – Yapay Zeka Destekli Gündem Analiz ve Haber Öneri Paneli

Bu proje, Türkiye’deki **popüler haber kanallarından güncel başlıkları** ve **Google Trends verilerini** çekerek, **BERTopic** ve **SentenceTransformer** gibi yapay zeka tabanlı NLP kütüphanelerini kullanıp, **güncel ve önerilen haber başlıkları** oluşturan bir sistemdir.  
Kullanıcıya tüm bu süreç, **Flask tabanlı bir web paneli** üzerinden grafikler ve tablolar ile sunulur.

---

## Proje Amacı
- Güncel gündemi belirleyen **haber başlıkları** ve **trend anahtar kelimeleri** toplamak.  
- **Doğal Dil İşleme (NLP)** teknikleriyle bu başlıklar üzerinde konu modelleme analizi yapmak.  
- **Kullanıcıya önerilen haber başlıklarını** yapay zekâ destekli olarak sunmak.  
- Kullanımı kolay, görselleştirilmiş bir **web paneli** ile sonuçları göstermek.

---

## Öne Çıkan Özellikler
- **RSS Kaynaklı Haber Toplama:** CNN Türk, Hürriyet, TRT Haber, Habertürk vb. kaynaklardan 15’er başlık çekilir.  
- **Google Trends Analizi:** Selenium tabanlı otomasyon ile Google Trends Türkiye verileri CSV formatında alınır.  
- **Yapay Zeka Destekli Analiz:**  
  - **SentenceTransformer** ile haber başlıkları vektörlere dönüştürülür.  
  - **CountVectorizer** ile stop-word temizleme ve kelime frekans analizi yapılır.  
  - **BERTopic** ile konular çıkarılır ve temsilci başlıklar belirlenir.  
- **Dinamik Veri Yönetimi:** Her çalıştırmada rastgele eklenmiş dosya isimleri (örn. `haber_gundemi_ab12cd34.csv`) oluşturularak eski veriler korunur.  
- **Web Paneli:** Flask + Chart.js + Bootstrap tabanlı arayüz.

---

## Teknolojiler
- **Backend:** Python 3.9+, Flask  
- **NLP:** `pandas`, `BERTopic`, `sentence-transformers`, `scikit-learn`  
- **Frontend:** Bootstrap 5, Chart.js  
- **Veri Toplama:** `feedparser` (RSS), `selenium`, `webdriver-manager`  
- **Yardımcı Araçlar:** `src/utils.py` içindeki `find_latest_csv`, `random_suffix`

---

**Nasıl Kullanılır**

- **Bash:**  
`python3 -m venv venv`  
`source venv/bin/activate  # Mac/Linux`  
`venv\Scripts\activate     # Windows`

- **Gereken Paketleri Kur**

- **Eğer Mac kullanıyorsan ve Selenium için chromedriver gerekiyorsa:**  
`brew install chromedriver`

- **1. Web Paneli Çalıştırma**  
`python app.py`  
Tarayıcıdan **http://localhost:5001** adresine gidin.

- **Komut Satırı (CLI) Kullanımı**  
`python main.py`

Bu komut:  
- Haber başlıklarını ve Google Trends verilerini toplar.  
- NLP analizini gerçekleştirir.  
- `data/analiz_sonuclari_<random>.csv` dosyasını oluşturur.



