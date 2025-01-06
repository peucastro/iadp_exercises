import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

# Calculate the average age by 'status' and 'sex' (rounded to one decimal place).


def solve():
    print((df.pivot_table(index="status", columns="sex", values="age", aggfunc="mean")).round(1))


solve()
