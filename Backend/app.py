from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("model/model.pkl")

@app.route("/")
def home():
    return "Dynamic Pricing API is running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        price = data["price"]
        competitor_price = data["competitor_price"]
        discount = data["discount"]
        rating = data["rating"]
        stock = data["stock"]
        views = data["views"]

        # 🔥 Feature Engineering (SAME AS TRAINING)
        price_diff = price - competitor_price
        price_ratio = price / (competitor_price + 1)
        stock_pressure = views / (stock + 1)
        discount_effect = discount * rating

        features = np.array([[
            price,
            competitor_price,
            discount,
            rating,
            stock,
            views,
            price_diff,
            price_ratio,
            stock_pressure,
            discount_effect
        ]])

        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0]

        # 🎯 Business Insight
        if prediction == 1:
            demand_label = "High Demand 🔥"
            suggestion = "Increase Price 📈"
        else:
            demand_label = "Low Demand ❄️"
            suggestion = "Decrease Price 📉"

        return jsonify({
            "prediction": demand_label,
            "confidence": float(max(probability)),
            "suggestion": suggestion
        })

    except Exception as e:
        return jsonify({"error": str(e)})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)