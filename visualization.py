import matplotlib.pyplot as plt
import os

def plot_sales(df):
    os.makedirs("images", exist_ok=True)

    plt.figure()
    plt.plot(df['date'], df['sales'], label='Actual')
    plt.plot(df['date'], df['predicted_sales'], label='Predicted')
    plt.legend()

    # Save first
    plt.savefig("images/sales_forecast.png")

    # ❌ REMOVE THIS BLOCKING LINE
    # plt.show()

    # ✅ Instead use this (non-blocking)
    plt.close()