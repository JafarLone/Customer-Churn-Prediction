# app_dashboard.py
import streamlit as st
import requests

# Define the URL of the Flask server
flask_url = 'http://127.0.0.1:5000/predict'

st.title('Customer Churn Prediction')

# Input fields for the user
monthly_spend = st.number_input('Monthly Spend', min_value=0)
total_purchase_frequency = st.number_input('Total Purchase Frequency', min_value=0)
tenure = st.number_input('Tenure', min_value=0)
customer_type = st.selectbox('Customer Type', ['Regular', 'VIP'])

# Map customer type to numerical values
customer_type_map = {'Regular': 0, 'VIP': 1}
customer_type_value = customer_type_map[customer_type]

if st.button('Predict'):
    # Send a POST request to the Flask server
    data = {
        'Feature1': monthly_spend,
        'Feature2': total_purchase_frequency,
        'Feature3': tenure,
        'Feature4': customer_type_value
    }
    try:
        response = requests.post(flask_url, json=data)
        result = response.json()
        st.write(f'Prediction: {"Churn" if result["prediction"] == 1 else "No Churn"}')
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
