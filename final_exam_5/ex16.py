import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

"""
Create a function 'ndias(date)' to calculate the number of days between the 'date' and today (2022-06-27).
Use this function within function solve() to create a new column 'days' with the number of days between the 'sold_date' and today (2022-06-27).
"""


def ndias(date):
    today = pd.Timestamp("2022-06-27")
    dias = (today - date).days
    return dias


def solve():
    df["days"] = df["sold_date"].apply(ndias)


solve()
print(df[~df["sold_date"].isna()].head(3))
