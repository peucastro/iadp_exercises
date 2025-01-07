import pandas as pd

df = pd.read_csv("f1_1.csv", encoding="utf-8", parse_dates=["dob", "date"])

# Calculate the mean of the number of 'points' for 'Lewis Hamilton'. (rounded to one decimal place)


def solve():
    aux = df.loc[df["name"] == "Lewis Hamilton"]
    print(aux["points"].mean().round(1))


solve()
