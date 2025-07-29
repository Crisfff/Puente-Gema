from flask import Flask, request, jsonify
import requests

MODEL_URL = "https://crisdeyvid-gema-ai-model.hf.space/predict"  # <--- Tu modelo real

app = Flask(name)

@app.route('/predict', methods=['POST'])
def predict():
    # Recibe texto plano del body
    data = request.get_data(as_text=True).strip()
    try:
        # Convierte a lista de floats
        features = [float(x.strip()) for x in data.split(",") if x.strip()]
    except Exception as e:
        return jsonify({"error": f"Error parsing input: {e}"}), 400

    # Envía a tu modelo como JSON
    payload = {"features": features}
    try:
        resp = requests.post(MODEL_URL, json=payload, timeout=15)
        result = resp.json()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"Error contacting model: {e}"}), 500

if name == "main":
    app.run(host='0.0.0.0', port=10000)
