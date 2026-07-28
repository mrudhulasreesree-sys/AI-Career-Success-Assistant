import streamlit as st

st.set_page_config(
    page_title="Interview Preparation",
    page_icon="🎤"
)

st.title("🎤 AI Interview Preparation")

career = st.selectbox(
    "Select Career",
    [
        "AI Engineer",
        "Software Developer",
        "Data Analyst"
    ]
)

if st.button("Show Interview Questions"):

    if career == "AI Engineer":

        st.subheader("AI Engineer Questions")

        st.write("1. What is Artificial Intelligence?")
        st.write("2. What is Machine Learning?")
        st.write("3. Difference between AI and ML?")
        st.write("4. Explain Supervised Learning.")
        st.write("5. What is Deep Learning?")

    elif career == "Software Developer":

        st.subheader("Software Developer Questions")

        st.write("1. What is Python?")
        st.write("2. Difference between List and Tuple?")
        st.write("3. Explain OOP Concepts.")
        st.write("4. What is a Function?")
        st.write("5. What is Exception Handling?")

    elif career == "Data Analyst":

        st.subheader("Data Analyst Questions")

        st.write("1. What is SQL?")
        st.write("2. What is Excel Pivot Table?")
        st.write("3. Difference between WHERE and HAVING?")
        st.write("4. What is Data Cleaning?")
        st.write("5. What is Data Visualization?")