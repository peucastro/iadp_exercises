import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

# Calculate the number of lines by 'Product line'.


def solve():
    print(df["Product line"].value_counts())


solve()
