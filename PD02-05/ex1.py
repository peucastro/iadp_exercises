import pandas as pd

df = pd.read_csv("gym_q1.csv", sep=";", parse_dates=["date"])


def solve():
    aux = df.loc[df["hours"] > 5]
    print(aux["age"].mean())


solve()
