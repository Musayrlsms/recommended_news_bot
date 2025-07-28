from src.haber import get_haberler
from src.trends import get_trends_csv
from src.gundem_analiz import analiz_et

def main():
    print("[1/3] Haberler çekiliyor...")
    haber_file = get_haberler()

    print("[2/3] Google Trends verisi çekiliyor...")
    trend_file = get_trends_csv()

    print("[3/3] Analiz yapılıyor...")
    analiz_file = analiz_et(haber_file, trend_file)

    print(f"🚀 Tüm süreç tamamlandı! Analiz dosyası: {analiz_file}")

if __name__ == "__main__":
    main()
