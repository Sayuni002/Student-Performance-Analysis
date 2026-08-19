import streamlit as st
import pandas as pd

df = pd.read_csv("data/student_data.csv")

st.title("Student Performance Analysis Dashboard")

st.write(
    "An interactive dashboard for analyzing student academic performance."
)

st.metric(
    "Total Students",
    len(df)
)

st.metric(
    "Average Final Grade",
    round(df["G3"].mean(), 2)
)

st.metric(
    "Highest Final Grade",
    df["G3"].max()
)

st.metric(
    "Average Absences",
    round(df["absences"].mean(), 2)
)


st.subheader("Average Grades")

average_grades = pd.DataFrame({
    "Grade": ["G1", "G2", "G3"],
    "Average": [
        df["G1"].mean(),
        df["G2"].mean(),
        df["G3"].mean()
    ]
})

st.bar_chart(
    average_grades.set_index("Grade")
)

st.subheader("Final Grade Distribution")


st.bar_chart(
    df["G3"].value_counts().sort_index()
)

st.subheader("Study Time vs Final Grade")

studytime_avg = df.groupby("studytime")["G3"].mean()

st.bar_chart(studytime_avg)


st.subheader("Previous Failures vs Final Grade")

failure_avg = df.groupby("failures")["G3"].mean()

st.bar_chart(failure_avg)


st.subheader("Absences vs Final Grade")

st.scatter_chart(
    df,
    x="absences",
    y="G3"
)