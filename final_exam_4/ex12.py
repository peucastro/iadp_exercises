import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

"""
Calculate the number of persons in each of the following 'age' classes:
[0, 20[ - very_young
[20, 40[ - young
[40, 60[ - middle_age
[60, 80[ - old
[80, 100[ - very_old
"""


def solve():
    bins = [0, 20, 40, 60, 80, 100]
    labels = ["very_young", "young", "middle_age", "old", "very_old"]
    df["age"] = pd.cut(df["age"], bins=bins, labels=labels, right=False)
    counts = df["age"].value_counts().sort_index()
    print(counts)


solve()
