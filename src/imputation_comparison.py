
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler

# 1. Load the original dataset
df = pd.read_excel("data/raw/Online Retail.xlsx")

# 2. Select valid records for this experiment
sample = df.loc[
    (df["UnitPrice"] > 0) & (df["Quantity"] > 0),
    ["Quantity", "UnitPrice"]
].dropna().sample(n=5000, random_state=42).copy()

# 3. Save the original prices for evaluation
true_prices = sample["UnitPrice"].copy()

# 4. Artificially hide 5% of prices
rng = np.random.default_rng(42)
missing_indices = rng.choice(
    sample.index.to_numpy(),
    size=int(len(sample) * 0.05),
    replace=False
)

sample.loc[missing_indices, "UnitPrice"] = np.nan

# 5. Mean imputation
mean_result = sample.copy()
mean_value = sample["UnitPrice"].mean()

mean_result["UnitPrice"] = (
    mean_result["UnitPrice"].fillna(mean_value)
)

# 6. Median imputation
median_result = sample.copy()
median_value = sample["UnitPrice"].median()

median_result["UnitPrice"] = (
    median_result["UnitPrice"].fillna(median_value)
)

# 7. Scale features before KNN imputation
scaler = StandardScaler()
scaled_values = scaler.fit_transform(sample[["Quantity", "UnitPrice"]])

# 8. Impute missing values using 5 nearest neighbours
imputer = KNNImputer(n_neighbors=5)
imputed_scaled = imputer.fit_transform(scaled_values)

# 9. Convert the scaled values back to original units
imputed_values = scaler.inverse_transform(imputed_scaled)

knn_result = sample.copy()
knn_result[["Quantity", "UnitPrice"]] = imputed_values

# 10. Compare predictions with the original hidden prices
actual = true_prices.loc[missing_indices]

imputed_prices = {
    "Mean": mean_result.loc[missing_indices, "UnitPrice"],
    "Median": median_result.loc[missing_indices, "UnitPrice"],
    "KNN": knn_result.loc[missing_indices, "UnitPrice"]
}

evaluation = []

for method, predictions in imputed_prices.items():
    evaluation.append({
        "Method": method,
        "MAE": mean_absolute_error(actual, predictions),
        "RMSE": np.sqrt(mean_squared_error(actual, predictions)),
        "Imputed Mean": predictions.mean(),
        "Actual Mean": actual.mean(),
        "Imputed Std": predictions.std(),
        "Actual Std": actual.std()
    })

results = pd.DataFrame(evaluation)

# 11. Display results
print("IMPUTATION METHOD COMPARISON")
print(results.round(4).to_string(index=False))

# 12. Save results
Path("outputs").mkdir(parents=True, exist_ok=True)

results.to_csv(
    "outputs/imputation_comparison.csv",
    index=False
)

print("\nResults saved to outputs/imputation_comparison.csv")
print(f"Sample size: {len(sample)}")
print(f"Artificially hidden prices: {len(missing_indices)}")
print("Original Excel dataset was not modified.")
