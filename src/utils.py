import os
import random
import string
import pandas as pd

def random_suffix(length=12):
    """Belirtilen uzunlukta rastgele bir harf-rakam karışımı string döndürür."""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def save_to_csv(filepath, data, headers=None):
    """Verilen veriyi belirtilen CSV dosyasına kaydeder."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df = pd.DataFrame(data, columns=headers if headers else None)
    df.to_csv(filepath, index=False, encoding='utf-8-sig')
    print(f"[INFO] {filepath} kaydedildi.")

def find_latest_csv(folder, keyword):
    """Klasördeki keyword içeren en son oluşturulmuş CSV dosyasını döndürür."""
    files = [f for f in os.listdir(folder) if f.endswith(".csv") and keyword in f]
    if not files:
        raise FileNotFoundError(f"{keyword} için CSV bulunamadı.")
    latest_file = max(files, key=lambda f: os.path.getctime(os.path.join(folder, f)))
    return os.path.join(folder, latest_file)
