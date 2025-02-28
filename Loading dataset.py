import pandas as pd

df = pd.read_csv("diabetes.csv")

print(df.head())

print("\nMissing Values:\n", df.isnull().sum())

print("\nDataset Info:\n", df.info())
