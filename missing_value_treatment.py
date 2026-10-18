from pathlib import Path

import pandas as pd

# Load original dataset
df = pd.read_excel("data/raw/Online Retail.xlsx")

# Record missing values before treatment
missing_before = df.isna().sum()

# Handle missing product descriptions transparently
df["Description"] = df["Description"].fillna(
    "Unknown Description"
)

# Keep missing CustomerID values unchanged.
# CustomerID is an identifier, so we should not invent IDs.

# Create output folder
output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

# Save the treated dataset separately
output_path = output_dir / "online_retail_missing_treated.csv"
df.to_csv(output_path, index=False)

# Report results
print("MISSING VALUE TREATMENT REPORT")
print("\nMissing values before treatment:")
print(missing_before[missing_before > 0])

print("\nMissing values after treatment:")
print(df.isna().sum()[df.isna().sum() > 0])

print(f"\nTreated dataset saved to: {output_path}")
print("Original Excel dataset was not modified.")