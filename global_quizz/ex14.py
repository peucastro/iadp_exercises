import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

# Calculate the percentage of Female and Male customers.


def solve():
    print(df["Gender"].value_counts(normalize=True) * 100)


solve()
