import pandas as pd

df = pd.read_csv("gym2_q1.csv", sep=";", index_col="id", parse_dates=["date"])


def solve():
    aux = df.loc[df["class"] == "pilates"]
    aux = aux.sort_values("hours", ascending=False)
    name = aux["name"].iloc[0]
    print(name)

solve()
