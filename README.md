# 📱 Mobile Device Usage and User Behavior

This project analyzes mobile device usage patterns to classify users into behavior classes (from light to extreme usage). It covers the full data science lifecycle—from data cleaning and EDA to building and deploying a machine learning model.

## 🧠 Objective

To explore, model, and predict user behavior based on mobile device usage data using a Random Forest Classifier and visualize insights through a Power BI dashboard and Flask web app.

---

## 📊 Dataset

- **Source**: [Kaggle Dataset](https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset)
- **Records**: 700 user entries
- **Features**:
  - Device Model
  - Operating System
  - App Usage Time (minutes/day)
  - Screen On Time (hours/day)
  - Battery Drain (mAh/day)
  - Number of Installed Apps
  - Data Usage (MB/day)
  - Age
  - Gender
  - User Behavior Class (Target Variable)

---

## ⚙️ Process Workflow

1. **Data Inspection** – Overview of features, missing values, data types  
2. **Data Cleaning** – Removing duplicates, handling outliers  
3. **Preprocessing** – Label encoding categorical data  
4. **Exploratory Data Analysis (EDA)** – Visualizations and insights on usage patterns  
5. **Feature Correlation** – Using heatmaps to study relationships  
6. **Model Building** – RandomForestClassifier (scikit-learn)  
7. **Model Evaluation** – Accuracy, classification report, confusion matrix  
8. **Deployment** – Flask web app with Heroku  
9. **Dashboard** – Power BI report for visualization

---

## ✅ Results

- The classifier demonstrated high accuracy and performance across all metrics.
- Strong correlation observed between screen-on time, app usage, battery drain, and behavior class.
- Flask app allows live user behavior class prediction based on inputs.
- Power BI dashboard provides dynamic data exploration and insights.

---

## 🚀 Live Demo

- 📊 **Power BI Dashboard**: [Power BI Report (If Available)](https://app.powerbi.com/links/oXRziRIj4i?ctid=77fd3202-9001-4147-b67d-4d5a95612546&pbi_source=linkShare&bookmarkGuid=baa4e860-1fdd-4b76-b6f6-f8c55eeb53bb)

---

## 🧰 Technologies Used

| Purpose                     | Tool/Library         |
|----------------------------|----------------------|
| Data Manipulation          | Pandas               |
| Data Visualization         | Matplotlib, Seaborn  |
| Machine Learning           | Scikit-learn         |
| Web Deployment             | Flask, Heroku        |
| Dashboard Visualization    | Power BI             |

---
