# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the data
data = pd.read_csv('customer_data.csv')

# Preprocess the data
data['CustomerType'] = data['CustomerType'].map({'Regular': 0, 'VIP': 1})
X = data[['MonthlySpend', 'TotalPurchaseFrequency', 'Tenure', 'CustomerType']]
y = data['Churn']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as model.pkl")
