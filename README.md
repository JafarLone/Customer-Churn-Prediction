# Customer Churn Prediction

**Customer Churn Prediction** is a machine learning project that aims to predict whether a customer will churn based on their spending patterns, purchase frequency, and tenure. The project involves training a predictive model using historical customer data and deploying it via a web application for real-time predictions.

![Customer Churn Prediction](images/image.jpg)

## Key Features

- **Model Training**: Utilizes a Random Forest Classifier to predict customer churn.
- **Real-Time Predictions**: A Flask API serves the trained model to provide predictions based on user input.
- **Interactive Dashboard**: Built with Streamlit to allow users to input customer data and receive instant churn predictions.

## Technologies

This project uses the following technologies:
- **Python**: For data processing, model training, and API development.
- **Flask**: To create a web API for serving predictions.
- **Streamlit**: To develop an interactive web dashboard.
- **Scikit-Learn**: For machine learning and model evaluation.
- **Pandas**: For data manipulation.

## How to Run

1. **Install Dependencies**:
   Ensure you have the necessary Python packages installed. You can install them using:
   ```bash
   pip install flask scikit-learn pandas streamlit requests
