# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

This project predicts house prices using Machine Learning techniques. A Linear Regression model is trained on housing data and deployed through an interactive Streamlit dashboard.

The application allows users to explore the dataset, visualize important patterns, evaluate model performance, and predict house prices based on property features.

---

## 🚀 Features

* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Interactive Visualizations
* Linear Regression Model
* House Price Prediction
* Model Evaluation using RMSE and R² Score
* Feature Importance Analysis
* Streamlit Dashboard

---

## 📊 Dataset Features

The model uses the following features:

* Bedrooms
* Bathrooms
* Square Feet Living Area (`sqft_living`)
* Square Feet Lot Area (`sqft_lot`)
* Floors
* Grade
* Square Feet Above Ground (`sqft_above`)
* Square Feet Basement (`sqft_basement`)
* Year Built (`yr_built`)

Target Variable:

* Price

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Plotly
* Streamlit

---

## 📈 Visualizations Included

### 1. House Price Distribution

Displays the distribution of house prices in the dataset.

### 2. Living Area vs Price

Shows the relationship between living area and house price.

### 3. Bedrooms vs Price

Analyzes how the number of bedrooms affects pricing.

### 4. Floors Distribution

Displays the number of houses based on floors.

### 5. Correlation Heatmap

Shows relationships between different features.

### 6. Actual vs Predicted Prices

Compares model predictions with actual values.

### 7. Feature Importance

Displays Linear Regression coefficients for each feature.

---

## 🤖 Machine Learning Model

### Linear Regression

The model learns the relationship between house features and price using Linear Regression.

### Evaluation Metrics

* RMSE (Root Mean Squared Error)
* R² Score

---

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── housing.csv
├── train_model.py
├── house_price_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/House-Price-Prediction.git
cd House-Price-Prediction
```

### Create Virtual Environment

```bash
python -m venv myenv
```

### Activate Environment

Windows:

```bash
myenv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Train Model

```bash
python train_model.py
```

This generates:

```text
house_price_model.pkl
```

---

## ▶️ Run Streamlit Application

```bash
streamlit run app.py
```

---

## 📸 Application Modules

### Dashboard

* Dataset overview
* Summary metrics
* Dataset preview

### EDA

* Distribution plots
* Scatter plots
* Heatmaps

### Model Evaluation

* RMSE
* R² Score
* Actual vs Predicted visualization
* Feature importance

### Prediction

* User input form
* Real-time house price prediction

---

## 📌 Future Improvements

* Random Forest Regression
* XGBoost Regression
* Hyperparameter Tuning
* Model Comparison Dashboard
* House Price Recommendation System
* Deployment on Streamlit Cloud

---

## 👩‍💻 Author

Khushi Agarwal

Machine Learning Internship Project
