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