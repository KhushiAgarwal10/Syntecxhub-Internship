# Spam Detection using Machine Learning

## Project Overview

This project is a Machine Learning-based Spam Detection System that classifies SMS messages as either Spam or Ham (Not Spam). The model is trained on a labeled SMS dataset using Natural Language Processing (NLP) techniques and Machine Learning algorithms.

## Objectives

* Load and analyze a spam/ham dataset.
* Preprocess text data by cleaning and tokenizing messages.
* Convert text into numerical features using TF-IDF Vectorization.
* Train a Machine Learning model for spam classification.
* Evaluate model performance using Precision, Recall, and F1-Score.
* Save the trained model for future predictions.

## Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* Scikit-learn
* Joblib

## Dataset

The project uses a labeled SMS Spam Collection dataset containing spam and ham messages.

## Project Workflow

1. Data Loading
2. Data Cleaning and Preprocessing
3. Text Tokenization
4. TF-IDF Feature Extraction
5. Model Training using Naive Bayes
6. Model Evaluation
7. Model Saving and Loading
8. Testing on New Messages

## Model Evaluation Metrics

* Accuracy Score
* Precision
* Recall
* F1-Score
* Classification Report

## Files Included

* `Spam_Detection.ipynb` – Complete project notebook
* `spam_detector.pkl` – Saved trained model
* `README.md` – Project documentation
* `spam.csv` – Dataset file (if included)

## Sample Prediction

Input:
"Congratulations! You have won a free prize."

Output:
Spam

Input:
"Hello, are we meeting in class today?"

Output:
Ham

## Future Improvements

* Compare multiple Machine Learning algorithms.
* Add a web-based user interface.
* Deploy the model using Flask or Streamlit.
* Improve text preprocessing and feature engineering.

## Conclusion

This project demonstrates the application of Natural Language Processing and Machine Learning techniques for spam message detection. The trained model can effectively classify messages and can be extended for real-world applications.
