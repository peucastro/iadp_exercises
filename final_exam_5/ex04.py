import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

# What is the percentage of houses with a 'house_size' greater than 2000. (rounded to one decimal place)


def solve():
    df_houses_count = df.shape[0]
    aux = df.loc[df["house_size"] > 2000]
    aux_houses_count = aux.shape[0]
    ans = aux_houses_count / df_houses_count * 100
    print(f"{ans:.1f}")


solve()
