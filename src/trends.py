import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from src.utils import random_suffix

def get_trends_csv(output_dir="data"):
    os.makedirs(output_dir, exist_ok=True)
    random_name = f"trending_{random_suffix()}.csv"
    output_file = os.path.join(output_dir, random_name)

    prefs = {
        "download.default_directory": os.path.abspath(output_dir),
        "download.prompt_for_download": False,
        "directory_upgrade": True
    }

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://trends.google.com/trending?geo=TR&hl=tr")
    wait = WebDriverWait(driver, 20)

    export_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(text(), 'Dışa aktar')]/ancestor::button")
    ))
    export_button.click()
    time.sleep(2)

    csv_download = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//li[@data-action='csv']")
    ))
    driver.execute_script("arguments[0].click();", csv_download)

    # Dosya indirildikten sonra ismini random ekle
    time.sleep(8)
    driver.quit()

    # İndirilen dosyayı bul ve yeniden adlandır
    downloaded_files = sorted(
        [f for f in os.listdir(output_dir) if f.endswith(".csv")],
        key=lambda x: os.path.getctime(os.path.join(output_dir, x)),
        reverse=True
    )
    if not downloaded_files:
        raise FileNotFoundError("CSV dosyası indirilemedi.")

    latest_download = os.path.join(output_dir, downloaded_files[0])
    os.rename(latest_download, output_file)
    print(f"✅ Google Trends CSV '{output_file}' içine indirildi.")
    return output_file
