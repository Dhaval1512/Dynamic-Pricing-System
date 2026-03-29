import React, { useState } from "react";
import axios from "axios";

function App() {
  const [formData, setFormData] = useState({
    price: "",
    competitor_price: "",
    discount: "",
    rating: "",
    stock: "",
    views: "",
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async () => {
    const price_diff = formData.competitor_price - formData.price;

    const features = [
      Number(formData.price || 0),
      Number(formData.competitor_price || 0),
      Number(formData.discount || 0),
      Number(formData.rating || 0),
      Number(formData.stock || 0),
      Number(formData.views || 0),
      Number(price_diff || 0)
    ];

    try {
      const response = await axios.post("https://dynamic-pricing-system-cfhm.onrender.com/predict", {
        features: features
      });

      setResult(response.data);
    } catch (error) {
      console.error("FULL ERROR:", error);

      if (error.response) {
        console.error("Backend Error:", error.response.data);
      }
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Dynamic Pricing Predictor 🚀</h1>

      {Object.keys(formData).map((key) => (
        <div key={key}>
          <input
            type="number"
            name={key}
            placeholder={key}
            onChange={handleChange}
          />
        </div>
      ))}

      <button onClick={handleSubmit}>Predict</button>

      {result && (
        <div>
          <h2>Prediction: {result.prediction}</h2>
          <h3>Probability: {result.probability[1]}</h3>
        </div>
      )}
    </div>
  );
}

export default App;