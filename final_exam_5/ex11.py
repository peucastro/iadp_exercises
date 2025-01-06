import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

# What is the 'city' with the house with the highest 'price' (first occurrence).


def solve():
    aux = df.sort_values("price", ascending=False)
    city = aux.iloc[0, 5]
    print(city)


solve()
