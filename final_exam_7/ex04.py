import pandas as pd

df = pd.read_csv("f1_1.csv", encoding="utf-8", parse_dates=["dob", "date"])

# Find the 'name' of the driver and the 'race' corresponding to the maximum 'fastest_lap_speed'. (rounded to one decimal place).


def solve():
    aux = df.sort_values("fastest_lap_speed", ascending=False)
    print(aux[["name", "race", "fastest_lap_speed"]].head(1).round(1))


solve()
