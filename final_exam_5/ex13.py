import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

# Find the average 'price' by 'state' and 'status' (rounded to one decimal place).


def solve():
    print(
        df.pivot_table(
            index="state", columns="status", values="price", aggfunc="mean"
        ).round(1)
    )


solve()
