import streamlit as st
import pandas as pd
import plotly.express as px
from database.database import view_students

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊"
)

st.title("📊 Student Dashboard")

students = view_students()

search = st.text_input("🔍 Search Student by Name")

if students:

    df = pd.DataFrame(
        students,
        columns=[
            "ID",
            "Name",
            "Age",
            "Gender",
            "Department",
            "CGPA",
            "Attendance"
        ]
    )
    if search:
        df = df[df["Name"].str.contains(search, case=False)]

    # ==========================
    # Student Table
    # ==========================
    st.dataframe(df, use_container_width=True)

    # ==========================
    # Summary Cards
    # ==========================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "👨‍🎓 Total Students",
            len(df)
        )

    with col2:
        st.metric(
            "⭐ Average CGPA",
            round(df["CGPA"].mean(), 2)
        )

    with col3:
        st.metric(
            "📅 Average Attendance",
            f"{round(df['Attendance'].mean(), 1)}%"
        )

    # ==========================
    # CGPA Chart
    # ==========================
    st.subheader("📊 CGPA Analysis")

    fig = px.bar(
        df,
        x="Name",
        y="CGPA",
        color="CGPA",
        title="Student CGPA"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ==========================
    # Attendance Chart
    # ==========================
    st.subheader("📈 Attendance Analysis")

    attendance_fig = px.line(
        df,
        x="Name",
        y="Attendance",
        markers=True,
        title="Student Attendance"
    )

    st.plotly_chart(attendance_fig, use_container_width=True)

    # ==========================
    # Department Pie Chart
    # ==========================
    st.subheader("🥧 Department Distribution")

    department_count = df["Department"].value_counts().reset_index()
    department_count.columns = ["Department", "Count"]

    pie_fig = px.pie(
        department_count,
        names="Department",
        values="Count",
        title="Students by Department"
    )

    st.plotly_chart(pie_fig, use_container_width=True)

else:
    st.warning("No students registered yet.")