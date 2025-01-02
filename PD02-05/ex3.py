import pandas as pd

df = pd.read_csv("gym_q1.csv", sep=";", parse_dates=["date"])


def solve():
    print(
        df.loc[
            ((df["sex"] == "M") & (df["height"] < 156)),
            ["name", "age", "height", "status"],
        ]
    )


solve()
