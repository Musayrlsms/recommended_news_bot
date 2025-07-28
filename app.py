from flask import Flask, render_template, jsonify
import pandas as pd
from main import main
from src.utils import find_latest_csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-analysis')
def run_analysis():
    main()  # Pipeline çalıştır

    # Analiz sonuç dosyasını bul ve oku
    analiz_file = find_latest_csv("data", "analiz_sonuclari")
    df = pd.read_csv(analiz_file)

    # Chart.js için JSON formatına dönüştür
    chart_labels = df["Topic"].astype(str).tolist() if "Topic" in df.columns else []
    chart_values = df["Count"].astype(int).tolist() if "Count" in df.columns else []

    return jsonify({
        "status": "ok",
        "message": "Analiz tamamlandı!",
        "table": df.to_html(classes="table table-striped", index=False),
        "labels": chart_labels,
        "values": chart_values
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
