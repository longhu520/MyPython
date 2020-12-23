import pandas as pd

df = pd.read_csv("dataset/data.csv")

print(df.head())

print(df["Name"].head())

fr_df = df[ df["Nationality"] == 'France' ].head()
print(fr_df)

print(fr_df.plot())