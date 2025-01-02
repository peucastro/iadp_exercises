import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

# Print the columns 'Product line' to 'Total' of the rows where the 'Total' is greater than 1030.


def solve():
    print(df.loc[(df["Total"] > 1030), ["Product line", "Total"]])


solve()
