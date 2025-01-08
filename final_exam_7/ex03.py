import pandas as pd

df = pd.read_csv("f1_1.csv", encoding="utf-8", parse_dates=["dob", "date"])

# Delete the columns 'code', 'fastest_lap_speed' and 'race'.


def solve():
    df.drop(["code", "fastest_lap_speed", "race"], axis=1, inplace=True)


solve()
print(df.head(3))
