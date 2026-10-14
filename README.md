
# Customer Spending Analysis

## Project Overview

Customer Spending Analysis is a data science project focused on data inspection, missing data analysis, imputation comparison, outlier treatment, feature engineering, and data visualization using the Online Retail dataset.

The project demonstrates practical data preprocessing and exploratory data analysis techniques using Python.

## Project Objectives

- Analyze missing values in the dataset.
- Compare Mean, Median, and KNN imputation methods.
- Identify and treat numerical outliers using the IQR method.
- Create new features from existing transaction data.
- Visualize unit price distributions, monthly sales values, and quantity-price relationships.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Excel / CSV

## Dataset

The project uses the Online Retail dataset from the UCI Machine Learning Repository.

Dataset source: https://archive.ics.uci.edu/dataset/352/online+retail

The original dataset contains retail transaction records, including invoice numbers, product codes, quantities, invoice dates, unit prices, customer IDs, and countries.

## Project Structure

```text
Customer_Spending_Analysis/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── outputs/
├── reports/
├── src/
│   ├── data_inspection.py
│   ├── missing_data_analysis.py
│   ├── numerical_analysis.py
│   ├── imputation_comparison.py
│   ├── outlier_analysis.py
│   ├── feature_engineering.py
│   └── visualize_data.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Key Tasks

### 1. Data Inspection
Examines the dataset structure, dimensions, column information, and missing values.

### 2. Missing Data Analysis
Identifies missing values and saves a report for further analysis.

### 3. Imputation Comparison
Compares Mean, Median, and KNN imputation using artificially hidden UnitPrice values. MAE, RMSE, and descriptive statistics are used for evaluation.

### 4. Outlier Analysis
Uses the Interquartile Range (IQR) method to identify outliers and caps extreme Quantity and UnitPrice values in a processed dataset. Non-positive quantities and unit prices are excluded from this analysis.

### 5. Feature Engineering
Creates additional features, including:
- TotalPrice
- InvoiceMonth
- InvoiceHour
- IsHighQuantity
- InvoiceYear
- InvoiceYearMonth

### 6. Data Visualization
Generates charts showing:
- Unit price distribution
- Monthly positive sales value over time
- Quantity versus unit price

## Installation

Install Python, then install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Run these commands from the project root directory:

```bash
python src/data_inspection.py
python src/missing_data_analysis.py
python src/numerical_analysis.py
python src/imputation_comparison.py
python src/outlier_analysis.py
python src/feature_engineering.py
python src/visualize_data.py
```

## Outputs

The project generates CSV reports, processed datasets, and visualization images in the `outputs/` and `data/processed/` directories.

The original Excel dataset is not modified by these scripts.

## Limitations

- The imputation comparison uses artificially hidden values because the original UnitPrice column has no missing values.
- Imputation results depend on the sample and evaluation method.
- Outlier capping changes extreme values in the processed dataset.
- The project focuses on data preprocessing and exploratory analysis; it does not train a machine learning prediction model.

## Conclusion

This project demonstrates practical data cleaning, imputation evaluation, outlier treatment, feature engineering, and visualization using Python. It provides a foundation for further data analysis and future predictive modeling.
