---

# 📩 SMS Spam Detection

A machine learning project that detects whether a given SMS message is **spam or not spam**. The model is built using **Python** and deployed using **Streamlit** for an interactive web interface.

---

## 🧠 Overview

* Developed a supervised machine learning model to classify SMS messages as spam or ham (not spam).
* Applied NLP techniques for text preprocessing and built multiple classification models.
* Deployed the best-performing model with a clean, responsive UI using Streamlit.

---

## 🛠️ Technology Stack

* **Python**
* **Pandas**, **NumPy**
* **Scikit-learn**
* **Streamlit**
* **Matplotlib**, **Seaborn** (for EDA & visualizations)

---

## ✨ Features

* SMS text classification (Spam / Not Spam)
* Data cleaning and preprocessing pipeline
* Exploratory Data Analysis with visualizations
* Model building and evaluation using multiple classifiers
* Web app deployment via Streamlit

---

## 📂 Dataset

* **Source:** [Kaggle - SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
* **Description:** Contains 5,500+ labeled SMS messages (spam or ham)

---

## 🧹 Data Cleaning & Preprocessing

* Removed null and duplicate entries
* Label encoding applied to target column
* Converted messages to lowercase
* Tokenized text and removed:

  * Special characters
  * Stop words
  * Punctuation
* Applied **stemming** to normalize words

---

## 📊 Exploratory Data Analysis

Performed EDA to extract insights and visualize message patterns:

* Character, word, and sentence counts
* Class distribution (spam vs. ham)
* Correlation heatmaps
* Word clouds for spam and ham messages
* Most frequent words visualized using bar plots

---

## 🤖 Model Building & Evaluation

Tested several machine learning models:

* **Naive Bayes**

**Best model:** Achieved **100% precision** on spam detection.

---

## 🌐 Web Deployment

* Deployed the model using **Streamlit**
* Interactive UI with a text input box
* Real-time prediction of spam or not spam messages

👉 [**Click here to try the app**](https://sms-spam-app.streamlit.app/)

---


