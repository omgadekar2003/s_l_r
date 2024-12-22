import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('linear_regression_model.pkl')

# Title of the Streamlit app
st.title("Linear Regression Prediction App")

# Description
st.write("This app predicts the output based on the input value using a trained Linear Regression model.")

# Input field for the user
input_value = st.number_input("Enter a feature value:", value=0.0, step=0.1)

# Predict button
if st.button("Predict"):
    try:
        # Make prediction
        prediction = model.predict(np.array([[input_value]]))
        st.success(f"Predicted Value: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
