import pandas as pd

df = pd.read_csv("f1_1.csv", encoding="utf-8", parse_dates=["dob", "date"])

# What is the percentage of races where 'Lewis Hamilton' has a 'status' of 'Finished' (rounded to one decimal place)


def solve():
    tot_races = df.loc[(df["name"] == "Lewis Hamilton")].shape[0]
    finished = df.loc[
        (df["name"] == "Lewis Hamilton") & (df["status"] == "Finished")
    ].shape[0]
    print(f"{finished / tot_races * 100:.1f}")


solve()
