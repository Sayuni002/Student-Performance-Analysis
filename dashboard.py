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



#  - FILTERS

st.sidebar.header("Student Filters")

gender_options = ["All"] + sorted(df["sex"].unique().tolist())

selected_gender = st.sidebar.selectbox(
    "Select Gender",
    gender_options
)

school_options = ["All"] + sorted(df["school"].unique().tolist())

selected_school = st.sidebar.selectbox(
    "Select School",
    school_options
)

studytime_options = ["All"] + sorted(
    df["studytime"].unique().tolist()
)

selected_studytime = st.sidebar.selectbox(
    "Select Study Time",
    studytime_options
)

filtered_df = df.copy()

if selected_gender != "All":
    filtered_df = filtered_df[
        filtered_df["sex"] == selected_gender
    ]

if selected_school != "All":
    filtered_df = filtered_df[
        filtered_df["school"] == selected_school
    ]

if selected_studytime != "All":
    filtered_df = filtered_df[
        filtered_df["studytime"] == selected_studytime
    ]

st.subheader("Filtered Student Summary")

st.metric(
    "Students Selected",
    len(filtered_df)
)

st.metric(
    "Filtered Average G3",
    round(filtered_df["G3"].mean(), 2)
)

st.metric(
    "Filtered Highest G3",
    filtered_df["G3"].max()
)

st.metric(
    "Filtered Average Absences",
    round(filtered_df["absences"].mean(), 2)
)

st.subheader("Study Time vs Final Grade")

studytime_avg = filtered_df.groupby("studytime")["G3"].mean()

st.bar_chart(studytime_avg)


st.subheader("Previous Failures vs Final Grade")

failure_avg = filtered_df.groupby("failures")["G3"].mean()

st.bar_chart(failure_avg)


st.subheader("Absences vs Final Grade")

st.scatter_chart(
    filtered_df,
    x="absences",
    y="G3"
)


st.subheader("Filtered Student Data")

st.dataframe(filtered_df)




