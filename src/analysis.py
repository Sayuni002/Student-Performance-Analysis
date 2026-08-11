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