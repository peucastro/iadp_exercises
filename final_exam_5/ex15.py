import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

"""
Calculate the number of houses in each of the following 'house_size' classes:
[0, 1000[ - very_small
[1000, 2000[ - small
[2000, 3000[ - medium
[3000, 5000[ - large
[5000, 10000[ - very_large
"""


def solve():
    labels = ["very_small", "small", "medium", "large", "very_large"]
    bins = [0, 1000, 2000, 3000, 5000, 10000]
    print(pd.cut(df["house_size"], bins, right=False, labels=labels).value_counts())


solve()
