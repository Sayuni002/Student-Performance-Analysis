import pandas as pd

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

