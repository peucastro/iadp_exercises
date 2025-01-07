import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

# What is the percentage of houses with a 'house_size' greater than 2000. (rounded to one decimal place)


def solve():
    print(f"{(df.loc[df["house_size"] > 2000].shape[0] / df.shape[0] * 100):.1f}")


solve()
