# Spam Detection System with Naive Bayes

A high-performance spam detection model built using Natural Language Processing (NLP) techniques and machine learning. This project uses TF-IDF vectorization and the Multinomial Naive Bayes algorithm to accurately classify messages as **spam** or **not spam**.

---

## Problem Statement

The internet is flooded with unwanted spam messages — from SMS to emails and comments on platforms like YouTube. Detecting and filtering these automatically is essential to protect users from scams, phishing, and clutter.

This project builds an effective spam classifier to distinguish between **not spam (legitimate)** and **spam** messages.

---

## Features

- Cleaned and preprocessed real-world datasets (SMS, YouTube, Email)
- TF-IDF vectorization of text
- Multiple models evaluated (Naive Bayes, Logistic Regression, SVM, etc.)
- Final model: **Multinomial Naive Bayes**
- Achieved **97%+ accuracy** and **1.0 precision**
- Pickled vectorizer and model for deployment
- Ready-to-use user input prediction script

---

## Model Selection

After experimenting with various classifiers (SVM, Logistic Regression, Decision Trees, etc.), **Multinomial Naive Bayes** was chosen due to its:

- High precision (1.0)
- Speed and scalability
- Natural compatibility with sparse text features (TF-IDF)

---

## Performance

| Model           | Accuracy | Precision |
|----------------|----------|-----------|
| MultinomialNB   | 0.9719   | 1.0000    |
| Random Forest   | 0.9700   | 0.9908    |
| Logistic Regression | 0.9613 | 0.9711    |
| Extra Trees     | 0.9778   | 0.9914    |

---

## Tech Stack

- Python 
- Scikit-learn
- NLTK
- Pandas / NumPy
- Matplotlib / Seaborn
- XGBoost (for experimentation)

---

## Text Preprocessing

- Lowercasing
- Tokenization
- Removing stopwords & punctuation
- Stemming
- TF-IDF Vectorization

---

## Demo
You can access the live demo of the application by visiting the following link:
[View Demo](https://spam-detection-jatin-wig.streamlit.app/)


