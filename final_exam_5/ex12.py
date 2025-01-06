import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

# Print the rows where the 'price' is greater than 2000000 and the 'house_size' is less or equal than 1000.


def solve():
    print(df.loc[(df["price"] > 2000000) & (df["house_size"] <= 1000)])


solve()
