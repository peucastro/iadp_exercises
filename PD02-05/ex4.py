import pandas as pd

df = pd.read_csv("gym_q1.csv", sep=";", parse_dates=["date"])


def solve():
    print(df["children"].value_counts().sort_index())


solve()
