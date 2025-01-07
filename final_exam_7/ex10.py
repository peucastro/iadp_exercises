import pandas as pd

df = pd.read_csv("f1_1.csv", encoding="utf-8", parse_dates=["dob", "date"])

# Who is the oldest ('dob') driver ('name') racing in 2021.


def solve():
    aux = df.loc[df["year"] == 2021]
    aux = aux.sort_values("dob")
    print(aux.iloc[0]["name"])


solve()
