import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/student_data.csv")

print(df)

print(df.head())

print(df.shape)

print(df.columns)

print(df.info())

print(df.describe())

print("Number of students:", len(df))

print("Average age:", df["age"].mean())

print("\nMissing values:")
print(df.isnull().sum())

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

print("\nStatistical summary:")
print(df.describe())

# Average grades
print("\nAverage G1:", df["G1"].mean())
print("Average G2:", df["G2"].mean())
print("Average G3:", df["G3"].mean())

# Highest and lowest final grades
print("\nHighest G3:", df["G3"].max())
print("Lowest G3:", df["G3"].min())

# Top 10 students based on final grade
top_students = df.sort_values("G3", ascending=False)

print("\nTop 10 students:")
print(top_students[["school", "sex", "age", "G1", "G2", "G3"]].head(10))

studytime_performance = df.groupby("studytime")["G3"].mean()

print("\nAverage final grade by study time:")
print(studytime_performance)

failure_performance = df.groupby("failures")["G3"].mean()

print("\nAverage final grade by number of failures:")
print(failure_performance)

print("\nAverage final grade by absence level:")

absence_performance = df.groupby("absences")["G3"].mean()

print(absence_performance)

gender_performance = df.groupby("sex")["G3"].mean()

print("\nAverage final grade by gender:")
print(gender_performance)

df["average_grade"] = (
    df["G1"] + df["G2"] + df["G3"]
) / 3



print("\nAverage grade of each student:")
print(df[["G1", "G2", "G3", "average_grade"]].head())

average_grades = [
    df["G1"].mean(),
    df["G2"].mean(),
    df["G3"].mean()
]

grade_names = [
    "G1",
    "G2",
    "G3"
]

plt.figure(figsize=(8, 5))

plt.bar(grade_names, average_grades)

plt.title("Average Student Grades")
plt.xlabel("Grade Period")
plt.ylabel("Average Grade")

plt.savefig("images/average_grades.png")

plt.show()




plt.figure(figsize=(8, 5))

plt.hist(df["G3"], bins=10)

plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")

plt.savefig("images/final_grade_distribution.png")

plt.show()



studytime_performance = df.groupby("studytime")["G3"].mean()

plt.figure(figsize=(8, 5))

plt.bar(
    studytime_performance.index.astype(str),
    studytime_performance.values
)

plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time Category")
plt.ylabel("Average Final Grade")

plt.savefig("images/studytime_vs_grade.png")

plt.show()



failure_performance = df.groupby("failures")["G3"].mean()

plt.figure(figsize=(8, 5))

plt.bar(
    failure_performance.index.astype(str),
    failure_performance.values
)

plt.title("Previous Failures vs Final Grade")
plt.xlabel("Number of Previous Failures")
plt.ylabel("Average Final Grade")

plt.savefig("images/failures_vs_grade.png")

plt.show()


plt.figure(figsize=(8, 5))

plt.scatter(df["absences"], df["G3"])

plt.title("Absences vs Final Grade")
plt.xlabel("Number of Absences")
plt.ylabel("Final Grade (G3)")

plt.savefig("images/absences_vs_grade.png")

plt.show()



# Create performance categories
def performance_level(score):
    if score >= 15:
        return "High"
    elif score >= 10:
        return "Medium"
    else:
        return "Low"


df["performance_level"] = df["G3"].apply(performance_level)

print("\nPerformance level distribution:")
print(df["performance_level"].value_counts())

performance_percentage = (
    df["performance_level"]
    .value_counts(normalize=True) * 100
)

print("\nPerformance percentages:")
print(performance_percentage)

higher_education = df.groupby("higher")["G3"].mean()

print("\nAverage G3 by higher education interest:")
print(higher_education)

school_support = df.groupby("schoolsup")["G3"].mean()

print("\nAverage G3 by school support:")
print(school_support)

family_support = df.groupby("famsup")["G3"].mean()

print("\nAverage G3 by family support:")
print(family_support)

summary = df.groupby("performance_level").agg(
    Average_G3=("G3", "mean"),
    Average_StudyTime=("studytime", "mean"),
    Average_Absences=("absences", "mean"),
    Average_Failures=("failures", "mean")
)

print("\nPerformance Summary:")
print(summary)


# DAY 7 - Advanced Visualizations


performance_counts = df["performance_level"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    performance_counts.index,
    performance_counts.values
)

plt.title("Student Performance Levels")
plt.xlabel("Performance Level")
plt.ylabel("Number of Students")

plt.savefig("images/performance_levels.png")

plt.show()

higher_education = df.groupby("higher")["G3"].mean()

plt.figure(figsize=(8, 5))

plt.bar(
    higher_education.index,
    higher_education.values
)

plt.title("Higher Education Interest vs Final Grade")
plt.xlabel("Interested in Higher Education")
plt.ylabel("Average Final Grade")

plt.savefig("images/higher_education_vs_grade.png")

plt.show()

school_support = df.groupby("schoolsup")["G3"].mean()

plt.figure(figsize=(8, 5))

plt.bar(
    school_support.index,
    school_support.values
)

plt.title("School Support vs Final Grade")
plt.xlabel("School Support")
plt.ylabel("Average Final Grade")

plt.savefig("images/school_support_vs_grade.png")

plt.show()

family_support = df.groupby("famsup")["G3"].mean()

plt.figure(figsize=(8, 5))

plt.bar(
    family_support.index,
    family_support.values
)

plt.title("Family Support vs Final Grade")
plt.xlabel("Family Support")
plt.ylabel("Average Final Grade")

plt.savefig("images/family_support_vs_grade.png")

plt.show()


plt.figure(figsize=(8, 5))

plt.scatter(df["G1"], df["G3"])

plt.title("First Period Grade vs Final Grade")
plt.xlabel("G1 - First Period Grade")
plt.ylabel("G3 - Final Grade")

plt.savefig("images/g1_vs_g3.png")

plt.show()

print("\nAverage Final Grade (G3):")
print(round(df["G3"].mean(), 2))

print("\nHighest Final Grade:")
print(df["G3"].max())

print("\nLowest Final Grade:")
print(df["G3"].min())


df["performance_level"]

print("\nPerformance Level Count:")
print(df["performance_level"].value_counts())

print("\nPerformance Level Percentage:")
print(
    (df["performance_level"].value_counts(normalize=True) * 100).round(2)
)

print("\nAverage G3 by Study Time:")
print(
    df.groupby("studytime")["G3"]
    .mean()
    .round(2)
)

print("\nAverage G3 by Previous Failures:")
print(
    df.groupby("failures")["G3"]
    .mean()
    .round(2)
)

df["absence_group"] = pd.cut(
    df["absences"],
    bins=[-1, 5, 10, 20, 100],
    labels=["Low", "Moderate", "High", "Very High"]
)

print("\nAverage G3 by Absence Group:")
print(
    df.groupby("absence_group", observed=False)["G3"]
    .mean()
    .round(2)
)

print("\nCorrelation with Final Grade (G3):")

correlation = df[
    ["G1", "G2", "studytime", "failures", "absences", "G3"]
].corr()["G3"].sort_values(ascending=False)

print(correlation.round(2))


print("\nAverage G3 by Higher Education Interest:")

print(
    df.groupby("higher")["G3"]
    .mean()
    .round(2)
)


print("\nAverage G3 by School Support:")

print(
    df.groupby("schoolsup")["G3"]
    .mean()
    .round(2)
)

print("\nAverage G3 by Family Support:")

print(
    df.groupby("famsup")["G3"]
    .mean()
    .round(2)
)

final_summary = pd.DataFrame({
    "Metric": [
        "Total Students",
        "Average G3",
        "Highest G3",
        "Lowest G3",
        "Average Absences",
        "Average Failures"
    ],
    
    "Value": [
        len(df),
        round(df["G3"].mean(), 2),
        df["G3"].max(),
        df["G3"].min(),
        round(df["absences"].mean(), 2),
        round(df["failures"].mean(), 2)
    ]
})

print("\n========== FINAL SUMMARY ==========")
print(final_summary)