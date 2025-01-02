import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

# Change the 'Customer type' in the third row from 'Normal' to 'Member'.


def solve():
    df.loc[2, ["Customer type"]] = ["Member"]


solve()
print(df.loc[:, "Invoice ID":"Gender"].head(3))
