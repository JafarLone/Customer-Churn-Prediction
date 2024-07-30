# Customer Churn Prediction

**Customer Churn Prediction** is a machine learning project that aims to predict whether a customer will churn based on their spending patterns, purchase frequency, and tenure. The project involves training a predictive model using historical customer data and deploying it via a web application for real-time predictions.

![Customer Churn Prediction](https://github.com/JafarLone/Customer-Churn-Prediction/blob/main/photo.png?raw=true)

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
2. **Prepare the Data**:
   Ensure the `customer_data.csv` file is located in the project directory. This file should contain the customer data required for training the model and making predictions. The file should have the following structure:
   ```csv
3. **Train the Model**:
   Run the following command to train the model:
   ```bash
   python train_model.py
4. **Run the Streamlit Dashboard**:
   In another terminal, start the Streamlit dashboard by running:
   ```bash
   streamlit run app_dashboard.py
5. **Using the Dashboard**:
   - Open the Streamlit app in your browser.
   - Enter customer data into the provided fields.
   - Click the "Predict" button to get the churn prediction result.

6. **API Requests**:
   You can also interact with the Flask API directly:
   - **Endpoint**: http://127.0.0.1:5000/predict
   - **Method**: POST
   - **Request Body**: JSON with customer data fields. Example:
     ```json
     {
       "MonthlySpend": 80,
       "TotalPurchaseFrequency": 25,
       "Tenure": 18,
       "CustomerType": "Regular"
     }
     ```

7. **Example Request**:
   Here is an example of how you can send a request to the API using `curl`:
   ```bash
   curl -X POST http://127.0.0.1:5000/predict \
        -H "Content-Type: application/json" \
        -d '{"MonthlySpend": 80, "TotalPurchaseFrequency": 25, "Tenure": 18, "CustomerType": "Regular"}'


