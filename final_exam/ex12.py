import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

"""
Calculate the number of products with 'Price' in each of the following classes:
[0, 100[ - very_low
[100, 200[ - low
[200, 300[ - normal
[300, 400[ - high
[400, 500[ - very_high
"""


def solve():
    bins = [0, 100, 200, 300, 400, 500]
    labels = ["very_low", "low", "normal", "high", "very_high"]
    print(
        pd.cut(df["Price"], bins=bins, labels=labels, right=False)
        .value_counts()
        .sort_index()
    )


solve()
