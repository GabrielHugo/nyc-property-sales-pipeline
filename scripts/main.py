from excel_reader import Extract

df = Extract("../data/nyc-rolling-sales.csv")

print(df.read_csv())