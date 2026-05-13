# 📱 Mobile Price Prediction using Machine Learning

## Introduction

Mobile phone pricing depends on several hardware and performance-related specifications such as RAM, processor power, display quality, storage capacity, battery size, and camera configuration. In this project, machine learning regression techniques are used to estimate the expected price of a smartphone based on its technical features.

The project demonstrates a complete end-to-end machine learning workflow including:

* Data cleaning
* Exploratory data analysis
* Feature preprocessing
* Regression model training
* Model evaluation
* Deployment preparation

---

## 🎯 Project Goal

The primary goal of this project is to build a predictive model capable of estimating mobile phone prices using device specifications.

This project can help:

* Understand which hardware specifications influence pricing most
* Predict approximate market value of a phone
* Demonstrate practical regression modeling techniques
* Build a real-world machine learning application workflow

---

## 🧠 Problem Type

This project is a:

### Supervised Machine Learning Regression Problem

The target variable is:

```text
Price
```

Since the output is numerical and continuous, regression algorithms were used.

---

## 📊 Dataset Overview

The dataset contains smartphone-related specifications and pricing information.

### Features Included

* Product ID
* RAM
* Internal Memory
* CPU Core
* CPU Frequency
* Rear Camera
* Front Camera
* Battery Capacity
* Screen Resolution
* PPI
* Thickness
* Weight
* Sales
* Price

### Dataset Characteristics

* 161 total records
* Numerical feature-based dataset
* No duplicate entries
* No missing values initially

The `Product_id` column was excluded from model training because it does not contribute to prediction.

---

## 🔍 Exploratory Data Analysis

Detailed exploratory analysis was performed to understand data patterns and feature relationships.

### Key Findings

* Mobile prices are distributed across budget, mid-range, and premium categories.
* RAM showed the strongest positive relationship with price.
* Internal memory and processor specifications significantly affected pricing.
* Display quality and camera specifications also contributed positively.
* Thickness showed a negative correlation with price.
* Certain columns contained unrealistic zero values which were treated as invalid entries.

### Data Quality Observations

Suspicious zero values were identified in:

* RAM
* Internal Memory
* CPU Frequency
* CPU Core

These values were handled carefully during preprocessing.

---

## ⚙️ Data Preprocessing

The following preprocessing pipeline was implemented:

### Preprocessing Steps

* Removed unnecessary identifier column
* Replaced suspicious zero values with median values
* Split data into training and testing datasets
* Applied feature scaling using `StandardScaler`
* Stored preprocessing objects for future deployment

### Dataset Split

| Dataset       | Percentage |
| ------------- | ---------: |
| Training Data |        80% |
| Testing Data  |        20% |

---

## 🤖 Machine Learning Models

Multiple regression models were trained and evaluated.

### Models Implemented

* Linear Regression
* Ridge Regression
* Lasso Regression
* ElasticNet Regression

### Evaluation Metrics

The models were compared using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

---

## 📈 Model Comparison

| Model                 | Test MAE | Test RMSE | Test R² |
| --------------------- | -------: | --------: | ------: |
| Linear Regression     |   136.10 |    166.74 |   0.951 |
| Ridge Regression      |   134.67 |    166.91 |   0.951 |
| Lasso Regression      |   135.00 |    166.65 |   0.951 |
| ElasticNet Regression |   165.57 |    219.26 |   0.915 |

---

## 🏆 Best Performing Model

### Ridge Regression

Ridge Regression achieved the best overall balance between prediction accuracy and model stability.

### Final Performance

```text
Test MAE  : 134.67
Test RMSE : 166.91
Test R²   : 95.1%
```

The model successfully explains most of the variance in mobile phone prices.

---

## 📉 Business Insights

Analysis from the project suggests:

* High RAM and larger internal memory are strong indicators of higher pricing.
* Premium smartphones tend to be thinner with better display quality.
* Better processor performance strongly increases estimated value.
* Camera quality contributes significantly to premium price ranges.

---

## 📊 Visualization & Analysis

The project includes multiple visual analyses such as:

### Visualizations Performed

* Price Distribution Analysis
* Feature Correlation Heatmap
* Actual vs Predicted Price Comparison
* Price Segment Analysis
* Feature Importance Relationships

These visualizations help interpret both the dataset and model behavior.

---

## 🛠️ Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core Programming Language |
| Pandas       | Data Manipulation         |
| NumPy        | Numerical Operations      |
| Scikit-learn | Machine Learning Models   |
| Matplotlib   | Data Visualization        |
| Seaborn      | Statistical Visualization |
| Pickle       | Model Serialization       |

---

## 🚀 Project Workflow

```text
Data Collection
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Preprocessing
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Prediction System
```

---

## ⚠️ Project Limitations

The current model does not include several real-world pricing factors such as:

* Mobile brand value
* Market demand
* Launch year
* Region-based pricing
* Discounts and promotional offers
* Operating system ecosystem

Because of this, predictions are mainly based on technical specifications.

---

## 🔮 Future Improvements

Potential enhancements for future versions:

* Add larger real-world datasets
* Include brand and model information
* Use advanced ensemble models
* Integrate deep learning techniques
* Add live market price tracking
* Build a production-ready web application

---

## ✅ Conclusion

This project demonstrates how machine learning regression techniques can be applied to estimate smartphone prices using hardware specifications.

The project successfully covers:

* Data preprocessing
* Exploratory analysis
* Regression modeling
* Model evaluation
* Prediction pipeline creation

Among all tested algorithms, Ridge Regression produced the most reliable performance on unseen data.

---

## 👨‍💻 Project Type

Machine Learning Regression Project
