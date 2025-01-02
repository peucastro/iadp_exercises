import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

# Insert a column named 'QxPrice' before column 'Tax 5%' equal to the column 'Unit price' times the column 'Quantity'.


def solve():
    df.insert(7, "QxPrice", df["Unit price"] * df["Quantity"])


solve()
print(df.loc[0:2, "Unit price":"Total"])
