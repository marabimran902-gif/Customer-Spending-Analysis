import pandas as pd

# Load the original dataset
file_path = "data/raw/Online Retail.xlsx"
df = pd.read_excel(file_path)

# Calculate missing values
missing_count = df.isnull().sum()

# Calculate missing percentage
missing_percentage = (missing_count / len(df)) * 100

# Create a summary table
missing_report = pd.DataFrame({
    "Missing Values": missing_count,
    "Missing Percentage": missing_percentage.round(2)
})

# Show columns that contain missing values
missing_report = missing_report[
    missing_report["Missing Values"] > 0
]

print("MISSING DATA ANALYSIS")
print(missing_report)

# Save the report
missing_report.to_csv(
    "outputs/missing_data_report.csv"
)

print("\nReport saved in outputs folder.")