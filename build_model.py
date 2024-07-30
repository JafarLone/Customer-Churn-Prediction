# build_model.py
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
data = pd.read_csv('customer_churn_data.csv')

# Data Preprocessing
data.fillna(method='ffill', inplace=True)  # Fill missing values
data = pd.get_dummies(data)  # Convert categorical variables to numerical

# Split data into features and target variable
X = data.drop('Churn', axis=1)
y = data['Churn']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model Building
model = RandomForestClassifier()
params = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20]
}

# Adjust cv for small datasets
grid_search = GridSearchCV(model, params, cv=2)  # Use cv=2 for small datasets
grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_

# Model Evaluation
y_pred = best_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the model
joblib.dump(best_model, 'churn_model.pkl')
