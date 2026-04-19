from excel_reader import ExtractTransform

df = ExtractTransform("../data/nyc-rolling-sales.csv")

print(df.transform())