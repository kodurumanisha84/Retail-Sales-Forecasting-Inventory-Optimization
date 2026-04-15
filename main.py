import os
from src.data_loader import load_data
from src.preprocessing import preprocess
from src.feature_engineering import create_features
from src.forecasting import train_model, predict
from src.inventory import inventory_optimization
from src.visualization import plot_sales

#  Create folders
os.makedirs("outputs", exist_ok=True)
os.makedirs("images", exist_ok=True)

# Load data
df = load_data("data/retail_sales.csv")

# Preprocess
df = preprocess(df)

# Feature Engineering
df = create_features(df)

# Train Model
model = train_model(df)

# Forecast
df = predict(model, df)

# Inventory Optimization
inventory_df = inventory_optimization(df)

# Visualization
plot_sales(df)

# Save outputs
df.to_csv("outputs/forecasts.csv", index=False)
inventory_df.to_csv("outputs/inventory_report.csv", index=False)

print("✅ Project Completed Successfully!")