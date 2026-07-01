# 🛍️ Customer Segmentation using K-Means Clustering

A Machine Learning project that segments mall customers into different groups based on their **Age**, **Annual Income**, and **Spending Score** using the **K-Means Clustering** algorithm. The goal is to help businesses understand customer behavior and create targeted marketing strategies.

---

## 📌 Project Overview

Customer segmentation is one of the most common applications of Unsupervised Machine Learning. Instead of predicting a target value, clustering algorithms discover hidden patterns within customer data.

In this project, customers are grouped into different segments using **K-Means Clustering**. The optimal number of clusters is determined using the **Elbow Method**, followed by visualization and analysis of each customer segment.

---

## 🎯 Objectives

* Load and preprocess the customer dataset.
* Clean and scale numerical features.
* Determine the optimal number of clusters using the Elbow Method.
* Apply the K-Means Clustering algorithm.
* Visualize customer clusters.
* Profile each cluster based on customer characteristics.
* Recommend marketing strategies for every customer segment.
* Save cluster labels for future analysis.

---

## 📂 Dataset

**Dataset:** Mall Customers Dataset

### Features

* Customer ID
* Gender
* Age
* Annual Income (k$)
* Spending Score (1–100)

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

---

## 📁 Project Structure

```text
Customer-Segmentation/
│
│── Mall_Customers.csv
│── Customer_Segmentation.ipynb
│── clustered_customers.csv
│── elbow_plot.png
│── clusters.png
│── customer_segment_report.pdf
├── README.md
```

---

## ⚙️ Project Workflow

1. Import required libraries.
2. Load the customer dataset.
3. Perform data cleaning.
4. Select important features.
5. Scale numerical features using StandardScaler.
6. Find the optimal number of clusters using the Elbow Method.
7. Train the K-Means clustering model.
8. Assign cluster labels to customers.
9. Visualize customer segments.
10. Analyze customer behavior for each cluster.
11. Recommend marketing strategies.
12. Export clustered dataset.

---

## 📊 Machine Learning Algorithm

### K-Means Clustering

K-Means is an unsupervised learning algorithm that groups similar data points into clusters based on distance from cluster centroids.

### Why K-Means?

* Simple and efficient
* Fast on medium-sized datasets
* Easy to interpret
* Widely used for customer segmentation

---

## 📈 Data Visualization

The project includes:

* Elbow Method Graph
* Customer Cluster Scatter Plot
* Cluster Profile Analysis

---

## 📋 Cluster Profiles

Example customer segments include:

### 🟢 Cluster 0 – Young High Spenders

**Characteristics**

* Young customers
* Moderate income
* High spending score

**Marketing Strategy**

* Loyalty rewards
* Premium products
* Exclusive discounts

---

### 🔵 Cluster 1 – High Income, Low Spending

**Characteristics**

* High income
* Low spending

**Marketing Strategy**

* Personalized recommendations
* Membership offers
* Targeted promotions

---

### 🟡 Cluster 2 – Average Customers

**Characteristics**

* Moderate income
* Moderate spending

**Marketing Strategy**

* Seasonal discounts
* Family offers
* Bundle deals

---

### 🔴 Cluster 3 – Premium Customers

**Characteristics**

* High income
* High spending

**Marketing Strategy**

* VIP memberships
* Luxury product promotions
* Early access to new collections

---

### 🟣 Cluster 4 – Budget Customers

**Characteristics**

* Low income
* Low spending

**Marketing Strategy**

* Budget-friendly products
* Coupons
* Cashback offers

---

## 📁 Output Files

The project generates:

* `clustered_customers.csv`
* `elbow_plot.png`
* `clusters.png`
* `customer_segment_report.pdf`

---

## 🚀 How to Run

### Clone the repository

```bash
git clone https://github.com/your-username/Customer-Segmentation.git
```

### Navigate to the project

```bash
cd Customer-Segmentation
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the notebook

```bash
jupyter notebook
```

Open `Customer_Segmentation.ipynb` and execute all cells.

---

## 📌 Results

* Successfully segmented customers into meaningful groups.
* Identified the optimal number of clusters using the Elbow Method.
* Visualized customer behavior based on income and spending score.
* Generated actionable marketing recommendations for each customer segment.
* Saved customer cluster labels for future business analysis.

---

## 🔮 Future Improvements

* Use PCA for dimensionality reduction.
* Compare K-Means with Hierarchical Clustering and DBSCAN.
* Build an interactive dashboard using Streamlit.
* Deploy the model as a web application.
* Add real-time customer prediction.

---

## 👩‍💻 Author

**Khushi Agarwal**

Machine Learning | Data Science | AI Enthusiast

---

## ⭐ If you found this project helpful, don't forget to Star the repository!
