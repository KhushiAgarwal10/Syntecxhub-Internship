import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# --------------------------
# Load Dataset
# --------------------------

df = pd.read_csv("housing.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# --------------------------
# Drop Unnecessary Columns
# --------------------------

df.drop(["id", "date"], axis=1, inplace=True)

# --------------------------
# Features & Target
# --------------------------

X = df[
    [
        "bedrooms",
        "bathrooms",
        "sqft_living",
        "sqft_lot",
        "floors",
        "grade",
        "sqft_above",
        "sqft_basement",
        "yr_built"
    ]
]

y = df["price"]

# --------------------------
# Train Test Split
# --------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# --------------------------
# Train Model
# --------------------------

model = LinearRegression()

model.fit(X_train, y_train)

# --------------------------
# Prediction
# --------------------------

y_pred = model.predict(X_test)

# --------------------------
# Evaluation
# --------------------------

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nModel Performance")
print("=" * 40)
print(f"RMSE : {rmse:,.2f}")
print(f"R² Score : {r2:.4f}")

# --------------------------
# Feature Coefficients
# --------------------------

coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print("\nFeature Importance")
print(coef_df)

# --------------------------
# Save Model
# --------------------------

with open("house_price_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel Saved Successfully!")

# --------------------------
# VISUALIZATIONS
# --------------------------

# Price Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["price"], kde=True)
plt.title("House Price Distribution")
plt.savefig("price_distribution.png")
plt.close()

# Living Area vs Price
plt.figure(figsize=(8,5))
sns.scatterplot(
    x=df["sqft_living"],
    y=df["price"]
)
plt.title("Living Area vs Price")
plt.savefig("living_area_vs_price.png")
plt.close()

# Bedrooms vs Price
plt.figure(figsize=(8,5))
sns.boxplot(
    x=df["bedrooms"],
    y=df["price"]
)
plt.title("Bedrooms vs Price")
plt.savefig("bedrooms_vs_price.png")
plt.close()


# Correlation Heatmap
plt.figure(figsize=(12,8))

sns.heatmap(
    df.corr(numeric_only=True),
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.close()

# Actual vs Predicted
plt.figure(figsize=(8,5))

plt.scatter(
    y_test,
    y_pred
)

plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")

plt.title("Actual vs Predicted")
plt.savefig("Actual_vs_Predicted.png")
plt.close()

# Feature Importance
plt.figure(figsize=(10,5))

sns.barplot(
    data=coef_df,
    x="Feature",
    y="Coefficient"
)

plt.xticks(rotation=45)

plt.title("Feature Coefficients")
plt.savefig("Feature_Coefficients.png")