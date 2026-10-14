
from pathlib import Path

import pandas as pd

# 1. Load the original dataset
df = pd.read_excel("data/raw/Online Retail.xlsx")

# 2. Select positive quantities and prices for analysis
analysis_df = df.loc[
    (df["Quantity"] > 0) & (df["UnitPrice"] > 0)
].copy()

# 3. Calculate original transaction-line value
analysis_df["TotalPrice"] = (
    analysis_df["Quantity"] * analysis_df["UnitPrice"]
)

# 4. Calculate IQR limits using the original analysis data
columns = ["Quantity", "UnitPrice", "TotalPrice"]
limits = {}
summary = []

for column in columns:
    q1 = analysis_df[column].quantile(0.25)
    q3 = analysis_df[column].quantile(0.75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    limits[column] = (lower, upper)

    original_outliers = (
        (analysis_df[column] < lower) |
        (analysis_df[column] > upper)
    ).sum()

    summary.append({
        "Column": column,
        "Lower Limit": lower,
        "Upper Limit": upper,
        "Outliers Before": int(original_outliers)
    })

# 5. Cap the original input columns at their IQR limits
for column in ["Quantity", "UnitPrice"]:
    lower, upper = limits[column]
    analysis_df[column] = analysis_df[column].clip(
        lower=lower,
        upper=upper
    )

# 6. Recalculate the derived value from treated input columns
analysis_df["TotalPrice"] = (
    analysis_df["Quantity"] * analysis_df["UnitPrice"]
)

# 7. Validate the treatment
for item in summary:
    column = item["Column"]
    lower, upper = limits[column]

    remaining = (
        (analysis_df[column] < lower) |
        (analysis_df[column] > upper)
    ).sum()

    item["Outliers After"] = int(remaining)

report = pd.DataFrame(summary)

# 8. Save the processed data and reports
Path("outputs").mkdir(parents=True, exist_ok=True)
Path("data/processed").mkdir(parents=True, exist_ok=True)

analysis_df.to_csv(
    "data/processed/online_retail_outlier_treated.csv",
    index=False
)

report.to_csv("outputs/outlier_report.csv", index=False)

# 9. Display results
print("IQR OUTLIER TREATMENT AND VALIDATION")
print(report.round(2).to_string(index=False))

print("\nPROCESSED DATA VALIDATION")
print(f"Rows processed: {len(analysis_df)}")
print(f"Missing values: {analysis_df.isnull().sum().sum()}")
print(
    "All Quantity values positive:",
    bool((analysis_df["Quantity"] > 0).all())
)
print(
    "All UnitPrice values positive:",
    bool((analysis_df["UnitPrice"] > 0).all())
)

print("\nProcessed data and report saved successfully.")
print("Original Excel dataset remains unchanged.")
