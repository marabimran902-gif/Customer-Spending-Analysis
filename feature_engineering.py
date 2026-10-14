
from pathlib import Path

import pandas as pd

# Load the original dataset
df = pd.read_excel("data/raw/Online Retail.xlsx")

# Ensure invoice dates are in datetime format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

# Feature 1: Value of each transaction line
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Feature 2: Month of the invoice
df["InvoiceMonth"] = df["InvoiceDate"].dt.month

# Feature 3: Hour of the invoice
df["InvoiceHour"] = df["InvoiceDate"].dt.hour

# Feature 4: Flag quantities greater than 10
df["IsHighQuantity"] = (df["Quantity"] > 10).astype(int)

# Additional feature 5: Invoice year
df["InvoiceYear"] = df["InvoiceDate"].dt.year

# Additional feature 6: Year-month for chronological analysis
df["InvoiceYearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)

# Display a sample of the engineered features
new_features = [
    "Quantity",
    "UnitPrice",
    "InvoiceDate",
    "TotalPrice",
    "InvoiceMonth",
    "InvoiceHour",
    "IsHighQuantity",
    "InvoiceYear",
    "InvoiceYearMonth"
]

print("FEATURE ENGINEERING RESULTS")
print(df[new_features].head(10).to_string(index=False))

# Create output directory if needed
Path("data/processed").mkdir(parents=True, exist_ok=True)

# Save without modifying the original Excel file
df.to_csv(
    "data/processed/online_retail_features.csv",
    index=False
)

print("\nFeature-engineered dataset saved successfully.")
print(f"Rows processed: {len(df)}")
print("Original Excel dataset remains unchanged.")
