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

  const [error, setError] = useState(null);

  const [loading, setLoading] = useState(false);

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async () => {
    setLoading(true);

    try {
      setError(null);
      const response = await axios.post("https://dynamic-pricing-system-cfhm.onrender.com/predict", {
        price: Number(formData.price),
        competitor_price: Number(formData.competitor_price),
        discount: Number(formData.discount),
        rating: Number(formData.rating),
        stock: Number(formData.stock),
        views: Number(formData.views)
      });

      setResult(response.data);
    } catch (error) {
      setError("Something went wrong. Please try again.");
      if (error.response) {
        console.error("Backend Error:", error.response.data);
      }
    }
    setLoading(false);
  };

  return (
  <div style={{ 
    display: "flex", 
    justifyContent: "center", 
    alignItems: "center", 
    height: "100vh",
    backgroundColor: "#f5f7fa"
  }}>
    <div style={{
      background: "white",
      padding: "30px",
      borderRadius: "12px",
      boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
      width: "350px"
    }}>
      <h2 style={{ textAlign: "center" }}>
        Dynamic Pricing Predictor 🚀
      </h2>

      {Object.keys(formData).map((key) => (
        <div key={key} style={{ marginBottom: "10px" }}>
          <label style={{ fontSize: "14px" }}>{key}</label>
          <input
            type="number"
            name={key}
            placeholder={key}
            onChange={handleChange}
            style={{
              width: "100%",
              padding: "8px",
              borderRadius: "6px",
              border: "1px solid #ccc"
            }}
          />
        </div>
      ))}

      <button 
        onClick={handleSubmit}
        disabled={loading}
        style={{
          width: "100%",
          padding: "10px",
          border: "none",
          borderRadius: "8px",
          backgroundColor: loading ? "#999" : "#4CAF50",
          color: "white",
          cursor: loading ? "not-allowed" : "pointer"
        }}
      >
        {loading ? "Predicting..." : "Predict"}
      </button>

      {/* 🔴 ERROR MESSAGE */}
      {error && (
        <p style={{ color: "red", marginTop: "10px" }}>
          {error}
        </p>
      )}

      {/* ✅ RESULT */}
      {result && (
        <div style={{
          marginTop: "20px",
          padding: "15px",
          borderRadius: "10px",
          backgroundColor: "#f1f3f5"
        }}>
          <h3>{result.prediction}</h3>
          <p>Confidence: {(result.confidence * 100).toFixed(2)}%</p>
          <p>{result.suggestion}</p>
        </div>
      )}
    </div>
  </div>
);
}

export default App;