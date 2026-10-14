import pandas as pd

# Load the original dataset
file_path = "data/raw/Online Retail.xlsx"
df = pd.read_excel(file_path)

# Select numerical columns
numeric_df = df.select_dtypes(include="number")

# Display summary statistics
print("NUMERICAL COLUMN SUMMARY")
print(numeric_df.describe().round(2))

# Count missing values in numerical columns
print("\nMISSING VALUES IN NUMERICAL COLUMNS")
print(numeric_df.isnull().sum())

# Check for non-positive quantities and prices
print("\nQUANTITY ZERO OR BELOW")
print((df["Quantity"] <= 0).sum())

print("\nUNIT PRICE ZERO OR BELOW")
print((df["UnitPrice"] <= 0).sum())