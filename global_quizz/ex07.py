import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

# Calculate a summary statistics of the column 'Total'. (rounded to two decimal places)


def solve():
    print(df["Total"].describe().round(2))


solve()
