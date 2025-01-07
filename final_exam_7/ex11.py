import pandas as pd

df = pd.read_csv("f1_1.csv", encoding="utf-8", parse_dates=["dob", "date"])

# Print the columns 'name' to 'year' for the rows where the 'year' is 2021  and the 'position' is equal to 1.


def solve():
    aux = df.loc[(df["year"] == 2021) & (df["position"] == 1)]
    print(aux.loc[:, "name":"year"])


solve()
