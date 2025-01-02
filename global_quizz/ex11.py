import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

# Print the rows between labels 0 and 2 and between columns 'Total' and 'Payment'.


def solve():
    print(df.loc[0:2, "Total":"Payment"])


solve()
