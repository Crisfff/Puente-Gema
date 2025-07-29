from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

MODEL_URL = "https://crisdeyvid-gema-ai-model.hf.space/predict"  # Tu modelo en HF Spaces

@app.route("/puente", methods=["POST"])
def puente():
    # Recibe texto plano, tipo: "38.0,118415.5,118416.2,30.2,82.9"
    try:
        texto = request.data.decode("utf-8")
        features = [float(x.strip()) for x in texto.split(",") if x.strip()]
        payload = {"features": features}
        r = requests.post(MODEL_URL, json=payload, timeout=15)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/", methods=["GET"])
def home():
    return "🚀 Puente activo: POST texto limpio a /puente", 200
