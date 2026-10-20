
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the feature-engineered dataset
df = pd.read_csv("data/processed/online_retail_features.csv")

# 2. Ensure the output directory exists
Path("outputs").mkdir(parents=True, exist_ok=True)

# 3. Set a consistent professional chart style
sns.set_theme(style="whitegrid", context="notebook")

# --------------------------------------------------
# Chart 1: Unit Price Distribution
# --------------------------------------------------
valid_prices = df.loc[df["UnitPrice"] > 0, "UnitPrice"].dropna()
price_limit = valid_prices.quantile(0.95)

plt.figure(figsize=(10, 6))
sns.histplot(
    valid_prices[valid_prices <= price_limit],
    bins=50,
    color="steelblue"
)
plt.title("Distribution of Unit Prices (Up to 95th Percentile)")
plt.xlabel("Unit Price")
plt.ylabel("Number of Transaction Lines")
plt.tight_layout()
plt.savefig("outputs/unit_price_distribution.png", dpi=300)
plt.close()

# --------------------------------------------------
# Chart 2: Monthly Positive Sales Value by Year-Month
# --------------------------------------------------
sales_df = df.loc[
    (df["TotalPrice"] > 0) & df["InvoiceYearMonth"].notna()
].copy()

monthly_sales = (
    sales_df.groupby("InvoiceYearMonth")["TotalPrice"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="bar", color="steelblue")
plt.title("Monthly Positive Sales Value Over Time")
plt.xlabel("Invoice Year-Month")
plt.ylabel("Positive Sales Value")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("outputs/monthly_sales.png", dpi=300)
plt.close()

# --------------------------------------------------
# Chart 3: Quantity vs Unit Price
# --------------------------------------------------
plot_df = df.loc[
    (df["Quantity"] > 0) & (df["UnitPrice"] > 0),
    ["Quantity", "UnitPrice"]
].dropna()

plot_df = plot_df.sample(
    n=min(3000, len(plot_df)),
    random_state=42
)

quantity_limit = plot_df["Quantity"].quantile(0.95)
scatter_price_limit = plot_df["UnitPrice"].quantile(0.95)

visible_data = plot_df.loc[
    (plot_df["Quantity"] <= quantity_limit)
    & (plot_df["UnitPrice"] <= scatter_price_limit)
]

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=visible_data,
    x="Quantity",
    y="UnitPrice",
    alpha=0.5
)
plt.title("Quantity vs Unit Price (Up to 95th Percentiles)")
plt.xlabel("Quantity")
plt.ylabel("Unit Price")
plt.tight_layout()
plt.savefig("outputs/quantity_vs_price.png", dpi=300)
plt.close()

# 4. Confirm that all charts were saved
print("All three visualizations saved successfully:")
print("- outputs/unit_price_distribution.png")
print("- outputs/monthly_sales.png")
print("- outputs/quantity_vs_price.png")
print("\nMonthly sales are grouped chronologically by year-month.")
print("The charts use selected display ranges for readability.")
