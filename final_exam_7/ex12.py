import pandas as pd

df = pd.read_csv("f1_1.csv", encoding="utf-8", parse_dates=["dob", "date"])

# Find the drivers 'name' and the number of times they finished a race in 1st, 2nd and 3rd positions for the year greater or equal 2018.


def solve():
    aux = df.loc[
        ((df["position"] == 1) | (df["position"] == 2) | (df["position"] == 3))
        & (df["year"] >= 2018)
    ]
    print(
        aux.pivot_table(
            index="name", columns="position", values="race_id", aggfunc="count"
        )
    )


solve()
