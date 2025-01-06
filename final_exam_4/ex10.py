import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

# Calculate the percentage of adults by 'status' (rounded to one decimal place) sorted in descending order.


def solve():
    aux = (df["status"].value_counts(normalize=True) * 100).round(1)
    print(aux)


solve()
