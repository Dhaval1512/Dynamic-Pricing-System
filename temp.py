import pandas as pd
import numpy as np

np.random.seed(42)
n = 2000

price = np.random.randint(10, 100, n)
competitor_price = np.random.randint(10, 100, n)
discount = np.random.randint(0, 50, n)
rating = np.round(np.random.uniform(2, 5, n), 1)
stock = np.random.randint(0, 500, n)
views = np.random.randint(50, 1000, n)

# 🔥 Feature Engineering
price_diff = competitor_price - price

# Hidden logic (real-world inspired)
demand_score = (
    0.4 * rating +
    0.003 * views +
    0.02 * discount +
    0.01 * price_diff -
    0.015 * price +
    0.001 * stock 
)

# Convert to classification
demand = (demand_score > np.median(demand_score)).astype(int)

df = pd.DataFrame({
    "price": price,
    "competitor_price": competitor_price,
    "discount": discount,
    "rating": rating,
    "stock": stock,
    "views": views,
    "price_diff": price_diff,
    "demand": demand
})

df.to_csv("data/data.csv", index=False)

print("Dataset created successfully!")