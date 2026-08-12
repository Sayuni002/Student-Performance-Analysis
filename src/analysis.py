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
