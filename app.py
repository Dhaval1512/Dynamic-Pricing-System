from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Load model once (important)
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "Dynamic Pricing API is running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        print("Incoming data:", data)

        features = np.array(data["features"]).reshape(1, -1)
        print("Features shape:", features.shape)
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0].tolist()
        
        return jsonify({
            "prediction": int(prediction),
            "probability": probability
        })
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)