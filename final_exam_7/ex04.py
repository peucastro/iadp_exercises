import pandas as pd

df = pd.read_csv("f1_1.csv", encoding="utf-8", parse_dates=["dob", "date"])

# Find the 'name' of the driver and the 'race' corresponding to the maximum 'fastest_lap_speed'. (rounded to one decimal place).


def solve():
    print(
        df.loc[
            df["fastest_lap_speed"] == df["fastest_lap_speed"].max(),
            ["name", "race", "fastest_lap_speed"],
        ].round(1)
    )


solve()
