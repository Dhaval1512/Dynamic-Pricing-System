import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data
df = pd.read_csv("data/data.csv")

X = df.drop("demand", axis=1)
y = df["demand"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Models
models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(n_estimators=100)
}

best_model = None
best_score = 0

# Train & Evaluate
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    
    acc = accuracy_score(y_test, preds)
    print(f"\n{name}")
    print("Accuracy:", acc)
    print(classification_report(y_test, preds))
    
    if acc > best_score:
        best_score = acc
        best_model = model

# Save best model
with open("model/model.pkl", "wb") as f:
    pickle.dump(best_model, f)

print("\nBest model saved!")