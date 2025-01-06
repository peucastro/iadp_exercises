import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

# Calculate the number of houses by 'status'.


def solve():
    print(df["status"].value_counts())


solve()
