import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("🎓 Student Performance Prediction App")
st.write("Enter student details to predict final score.")

# User inputs
study_hours = st.number_input("Study Hours per Day", min_value=1, max_value=12, value=5)
attendance = st.number_input("Attendance Percentage", min_value=50, max_value=100, value=80)
previous_score = st.number_input("Previous Exam Score", min_value=0, max_value=100, value=65)

# Prediction
if st.button("Predict Final Score"):
    input_data = np.array([[study_hours, attendance, previous_score]])
    prediction = model.predict(input_data)
    st.success(f"📊 Predicted Final Score: {prediction[0]:.2f}")
