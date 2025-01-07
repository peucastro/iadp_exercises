import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

# Delete the column 'Customer type'.


def solve():
    df.drop("Customer type", axis=1, inplace=True)


solve()
print(df.loc[:, "Invoice ID":"Gender"].head(3))
