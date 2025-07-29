from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

MODEL_URL = "https://crisdeyvid-gema-ai-model.hf.space/predict"

@app.route("/predict", methods=["POST"])
def predict():
    # Recibe valores en texto plano (separados por comas)
    features_text = request.data.decode("utf-8").strip()
    try:
        features = [float(x.strip()) for x in features_text.split(",") if x.strip()]
    except Exception as e:
        return jsonify({"error": f"Error parsing features: {e}"}), 400

    payload = {"features": features}
    try:
        response = requests.post(MODEL_URL, json=payload, timeout=15)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": f"Error contacting model: {e}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
