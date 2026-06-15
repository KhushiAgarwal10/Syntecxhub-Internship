import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 House Price Prediction Dashboard")



df = pd.read_csv("housing.csv")

df.drop(["id", "date"], axis=1, inplace=True)

# Features
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

# ----------------------------
# LOAD MODEL
# ----------------------------

with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# ----------------------------
# EVALUATION
# ----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)


menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "EDA",
        "Model Evaluation",
        "Prediction"
    ]
)


if menu == "Dashboard":

    st.header("📊 Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Houses", len(df))
    c2.metric("Average Price", f"₹{df['price'].mean():,.0f}")
    c3.metric("Average Living Area", f"{df['sqft_living'].mean():,.0f}")
    c4.metric("Features", X.shape[1])

    st.subheader("Dataset Preview")
    st.dataframe(df.head())



elif menu == "EDA":

    st.header("📈 Exploratory Data Analysis")

    st.subheader("Price Distribution")

    fig, ax = plt.subplots()
    sns.histplot(df["price"], kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("Living Area vs Price")

    fig = px.scatter(
        df,
        x="sqft_living",
        y="price",
        title="Living Area vs Price"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Bedrooms vs Price")

    fig = px.box(
        df,
        x="bedrooms",
        y="price"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Correlation Heatmap")

    fig, ax = plt.subplots(figsize=(12,8))

    sns.heatmap(
        df.corr(numeric_only=True),
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)


elif menu == "Model Evaluation":

    st.header("📉 Model Evaluation")

    c1, c2 = st.columns(2)

    c1.metric("RMSE", f"{rmse:,.0f}")
    c2.metric("R² Score", round(r2, 3))

    st.subheader("Actual vs Predicted")

    fig = px.scatter(
        x=y_test,
        y=y_pred,
        labels={
            "x": "Actual Price",
            "y": "Predicted Price"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Feature Coefficients")

    coef_df = pd.DataFrame({
        "Feature": X.columns,
        "Coefficient": model.coef_
    })

    st.dataframe(coef_df)

    fig = px.bar(
        coef_df,
        x="Feature",
        y="Coefficient",
        title="Feature Importance"
    )

    st.plotly_chart(fig, use_container_width=True)



elif menu == "Prediction":

    st.header("🔮 Predict House Price")

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=10,
        value=3
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1.0,
        max_value=10.0,
        value=2.0
    )

    sqft_living = st.number_input(
        "Living Area (sqft)",
        min_value=500,
        value=2000
    )

    sqft_lot = st.number_input(
        "Lot Area (sqft)",
        min_value=1000,
        value=5000
    )

    floors = st.number_input(
        "Floors",
        min_value=1.0,
        max_value=5.0,
        value=2.0
    )

    grade = st.number_input(
        "Grade",
        min_value=1,
        max_value=13,
        value=7
    )

    sqft_above = st.number_input(
        "Sqft Above",
        min_value=500,
        value=1500
    )

    sqft_basement = st.number_input(
        "Sqft Basement",
        min_value=0,
        value=500
    )

    yr_built = st.number_input(
        "Year Built",
        min_value=1900,
        max_value=2025,
        value=2000
    )

    if st.button("Predict Price"):

        features = [[
            bedrooms,
            bathrooms,
            sqft_living,
            sqft_lot,
            floors,
            grade,
            sqft_above,
            sqft_basement,
            yr_built
        ]]

        prediction = model.predict(features)

        st.success(
            f"🏠 Predicted House Price: ₹ {prediction[0]:,.2f}"
        )

    st.subheader("Example Predictions")

    sample_df = pd.DataFrame({
        "bedrooms": [3,4,5],
        "bathrooms": [2,3,4],
        "sqft_living": [2000,3000,4000],
        "sqft_lot": [5000,7000,10000],
        "floors": [2,2,3],
        "grade": [7,8,9],
        "sqft_above": [1500,2500,3200],
        "sqft_basement": [500,500,800],
        "yr_built": [2000,2010,2015]
    })

    sample_df["Predicted Price"] = model.predict(sample_df)

    st.dataframe(sample_df)