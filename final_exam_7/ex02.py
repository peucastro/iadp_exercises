import pandas as pd

df = pd.read_csv("f1_1.csv", encoding="utf-8", parse_dates=["dob", "date"])

# Change in row 2 the 'status' to 'Engine' and the 'points' to 0.


def solve():
    global df
    df.loc[2, "status"] = "Engine"
    df.loc[2, "points"] = 0


solve()
print(df.loc[:, "name":"status"].head(3))
