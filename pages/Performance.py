import streamlit as st
import joblib

st.set_page_config(
    page_title="Performance Prediction",
    page_icon="📈"
)

st.title("📈 AI Performance Prediction")

cgpa = st.number_input(
    "Enter CGPA",
    0.0,
    10.0
)

attendance = st.slider(
    "Attendance %",
    0,
    100
)

if st.button("Predict"):

    model = joblib.load("models/performance_model.pkl")

    prediction = model.predict([[cgpa, attendance]])

    st.success(f"Predicted Performance : {prediction[0]}")