import streamlit as st
from database.database import insert_student

st.set_page_config(page_title="Register", page_icon="📝")

st.title("📝 Student Registration")

name = st.text_input("Student Name")

age = st.number_input(
    "Age",
    min_value=16,
    max_value=40,
    step=1
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

department = st.selectbox(
    "Department",
    [
        "Artificial Intelligence",
        "Computer Science",
        "Information Technology",
        "Electronics"
    ]
)

cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0
)

attendance = st.slider(
    "Attendance %",
    0,
    100
)

if st.button("Register"):

    insert_student(
        name,
        age,
        gender,
        department,
        cgpa,
        attendance
    )

    st.success("Student Registered Successfully!")