import pandas as pd
x = 'T01'
df = pd.read_csv("input.csv", sep = ",")
print(df[df["sectorname"].str.contains("T01", na=False)])
