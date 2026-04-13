# customer-churn-ml-project
Machine Learning project to predict customer churn with Flask deployment
# Customer Churn Prediction

##  Overview
This project predicts whether a customer will churn using machine learning techniques and deploys the model using a Flask web application.


##  Problem Statement
Customer churn is a major issue for telecom companies. This project aims to predict customer churn based on usage and billing data.


##  Dataset
Telco Customer Churn Dataset containing:
- Tenure
- Monthly Charges
- Total Charges
- Churn (target)


## Data preprocessing
- Converted TotalCharges to numeric
- Handled missing values using median imputation
- Encoded target variable (Yes → 1, No → 0)


##  Models used
- Logistic Regression
- Decision Tree
- Random Forest (Final Model)

---

## Evaluation metrics
- Accuracy
- Precision
- Recall

---

## Final Model
Random Forest was selected based on its strong performance.

---

## Deployment
The model is deployed using Flask and allows real time predictions through a web interface.

---

## How to run
1. Clone the repo
2. Install dependencies:
