import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("../data/data.csv")

# -----------------------------
# Feature Engineering
# -----------------------------
df['price_diff'] = df['price'] - df['competitor_price']
df['price_ratio'] = df['price'] / (df['competitor_price'] + 1)
df['stock_pressure'] = df['views'] / (df['stock'] + 1)
df['discount_effect'] = df['discount'] * df['rating']

# Features
features = [
    'price',
    'competitor_price',
    'discount',
    'rating',
    'stock',
    'views',
    'price_diff',
    'price_ratio',
    'stock_pressure',
    'discount_effect'
]

X = df[features]
y = df['demand']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Pipeline (IMPORTANT)
# -----------------------------
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier())
])

# Train
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
print("\nModel Evaluation:\n")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(pipeline, "model/model.pkl")

print("\n✅ Model trained and saved successfully!")