import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

"""
Using the Pandas library create a function 'solve()' to answer the following:
Calculate the number of Invoices in each of the following 'Total' classes:
[0, 220[ - low
[220, 440[ - fair
[440, 660[ - good
[660, 880[ - very_good
[880, 1100[ - excellent
"""


def solve():
    data = df["Total"]
    bins = [0, 220, 440, 660, 880, 1100]
    labels = ["low", "fair", "good", "very_good", "excellent"]
    ans = pd.cut(data, bins=bins, labels=labels, right=False)
    print(ans.value_counts())


solve()
