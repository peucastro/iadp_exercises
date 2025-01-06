import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

# Delete the columns 'bed' to 'acre_lot'.


def solve():
    df.drop(columns=["bed", "bath", "acre_lot"], inplace=True)


solve()
print(df.head(3))
