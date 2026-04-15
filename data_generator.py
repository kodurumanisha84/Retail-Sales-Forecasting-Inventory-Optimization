import pandas as pd
import numpy as np
import os

os.makedirs("data", exist_ok=True)

np.random.seed(42)

dates = pd.date_range(start="2023-01-01", periods=150)

products = ["Milk", "Bread", "Eggs", "Rice", "Oil"]

data = []

for date in dates:
    for product in products:
        base_sales = np.random.randint(80, 200)
        
        if date.weekday() >= 5:
            base_sales += 30
        
        trend = date.dayofyear * 0.3
        noise = np.random.randint(-15, 15)
        
        sales = int(base_sales + trend + noise)
        
        data.append([date, product, sales])

df = pd.DataFrame(data, columns=["date", "product", "sales"])

df.to_csv("data/retail_sales.csv", index=False)

print("✅ Multi-product dataset created:", df.shape)