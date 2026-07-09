# 🎬 Movie Recommendation System

## 📌 Overview

The Movie Recommendation System is a Machine Learning project that recommends movies based on their content. It uses movie metadata such as genres, keywords, cast, crew, and overview to find similar movies using **TF-IDF Vectorization** and **Cosine Similarity**.

This project is built with **Python** and includes a simple **Streamlit** web application for an interactive user experience.

---

## 🚀 Features

* Content-Based Movie Recommendation
* Data Cleaning and Preprocessing
* Text Processing using NLTK
* TF-IDF Vectorization
* Cosine Similarity for Recommendation
* Interactive Streamlit User Interface
* Easy to Use and Extend

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit
* Pickle

---

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── data_cleaning.py
├── nltk_processing.py
├── recommendation.py
├── app.py
├── requirements.txt
├── cleaned_movies.csv
├── processed_movies.csv
├── movies.pkl
├── similarity.pkl
└── README.md
```

---

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset**.

Files required:

* tmdb_5000_movies.csv
* tmdb_5000_credits.csv

---

## ⚙️ Project Workflow

1. Load the TMDB datasets.
2. Merge movie and credits data.
3. Clean and preprocess the data.
4. Extract genres, cast, crew, keywords, and overview.
5. Create a combined text feature (`tags`).
6. Apply NLTK stemming.
7. Convert text into TF-IDF vectors.
8. Compute Cosine Similarity.
9. Recommend the top 5 similar movies.
10. Display recommendations using a Streamlit web application.

---

## ▶️ Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Step 1:

```bash
python data_cleaning.py
```

Step 2:

```bash
python nltk_processing.py
```

Step 3:

```bash
python recommendation.py
```

Step 4:

```bash
streamlit run app.py
```

---

## 💻 Sample Recommendation

**Input**

```
Avatar
```

**Output**

```
Guardians of the Galaxy
John Carter
Star Trek
Alien
Planet of the Apes
```

---

## 📈 Machine Learning Techniques

* Content-Based Recommendation
* Feature Engineering
* TF-IDF Vectorization
* Cosine Similarity
* Natural Language Processing (NLP)

---

## 🎯 Future Improvements

* Display movie posters using the TMDB API.
* Add movie search suggestions.
* Filter recommendations by genre.
* Deploy the application on Streamlit Community Cloud.
* Add user ratings and collaborative filtering.

---

## 👩‍💻 Author

**Khushi Agarwal**

B.Tech Computer Science Engineering

COER University

---

## 📜 License

This project is developed for educational and learning purposes.
