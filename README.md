# Customer Churn Prediction

## Overview

This project predicts whether an e-commerce customer will churn using machine learning techniques and deploys the model using a Flask web application.

## Problem Statement

Customer churn is a major issue for e-commerce companies. Acquiring a new customer costs significantly more than retaining an existing one. This project aims to predict customer churn based on behavioral and demographic data, so the business can take proactive action to retain at-risk customers.

## Dataset

E-Commerce Customer Churn Dataset from Kaggle containing approximately 5,000 rows and 20 columns.

Download link: https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction

Key columns:

- Tenure
- SatisfactionScore
- Complain
- CashbackAmount
- DaySinceLastOrder
- PreferredPaymentMode
- Churn (target)

## Data Preprocessing

- Loaded the correct sheet from the Excel file (E Comm)
- Checked and handled missing values using median imputation for numeric columns and mode imputation for categorical columns
- Removed duplicate rows
- Dropped the CustomerID column as it is not useful for prediction
- Encoded all categorical variables using LabelEncoder

## Feature Engineering

Three new features were created:

- ComplaintsPerOrder: number of complaints relative to number of orders
- EngagementScore: tenure divided by days since last order, measures how recently active the customer is
- SatisfactionRisk: cashback amount divided by satisfaction score, flags customers receiving high cashback despite low satisfaction

## Feature Selection

Used the Filter Method (SelectKBest with ANOVA F-test) to select the top 15 most informative features based on their ability to separate churned from non-churned customers.

## Models Used

- Logistic Regression
- Decision Tree
- Random Forest (Final Model)

All three models were trained and compared. Random Forest was selected based on its strongest performance across all metrics.

## Parameter Tuning

GridSearchCV was used to tune the Random Forest model across the following parameters:

- n_estimators: number of trees
- max_depth: maximum depth per tree
- min_samples_split: minimum samples required to split a node
- class_weight: to handle class imbalance

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

## Final Model

The tuned Random Forest model achieved Precision and Recall both above 0.3, meeting the project requirements.

## Deployment

The model is deployed using Flask and allows real-time predictions through a web interface with dropdowns and sliders for easy input.

Live link: https://customer-churn-predictor.onrender.com

## How to Run

1. Install dependencies:

```
pip install pandas numpy matplotlib seaborn scikit-learn joblib flask openpyxl
```

2. Run the notebook to generate the saved model files:

```
notebook.ipynb
```

3. Run the web app:

```
python app.py
```

4. Open in browser:

```
http://127.0.0.1:5000
```

## Author

Romaisaa Mohamed
221000583
