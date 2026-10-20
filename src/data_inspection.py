# Import the pandas library
import pandas as pd

# Define the path of our Excel dataset
file_path = "data/raw/Online Retail.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Display the first five rows
print("FIRST FIVE ROWS:")
print(df.head())

# Display the number of rows and columns
print("\nDATASET SHAPE:")
print(df.shape)

# Display column names and data types
print("\nDATASET INFORMATION:")
df.info()

# Count missing values in each column
print("\nMISSING VALUES:")
print(df.isnull().sum())