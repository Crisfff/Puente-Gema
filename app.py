from flask import Flask, request, jsonify

app = Flask(name)

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener el texto plano del body
    data = request.get_data(as_text=True).strip()
    try:
        # Convertir los valores a float
        features = [float(x.strip()) for x in data.split(",") if x.strip()]
    except Exception as e:
        return jsonify({"error": f"Error parsing input: {e}"}), 400

    # --- Aquí harías el request a tu modelo IA, pero vamos a simular la respuesta ---
    # Ejemplo de respuesta
    output = {
        "input": features,
        "signal": "CALL" if sum(features) > 0 else "PUT",  # Simula lógica
        "confianza": "99.9%"
    }
    return jsonify(output)

if name == 'main':
    app.run(host='0.0.0.0', port=10000)
