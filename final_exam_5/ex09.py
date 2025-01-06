import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

# Print the top 3 houses in 'price'.


def solve():
    aux = df.sort_values("price", ascending=False)
    print(aux.head(3))


solve()
