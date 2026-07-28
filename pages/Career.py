import streamlit as st

st.set_page_config(
    page_title="Career Recommendation",
    page_icon="💼"
)

st.title("💼 AI Career Recommendation")

performance = st.selectbox(
    "Select Student Performance",
    [
        "Excellent",
        "Good",
        "Average",
        "Poor"
    ]
)

if st.button("Recommend Career"):

    if performance == "Excellent":
        st.success("🌟 Recommended Career: AI Engineer / Data Scientist")

    elif performance == "Good":
        st.info("💻 Recommended Career: Software Developer / Data Analyst")

    elif performance == "Average":
        st.warning("🌐 Recommended Career: Web Developer / QA Engineer")

    else:
        st.error("📚 Recommendation: Improve your skills before choosing a specialization.")