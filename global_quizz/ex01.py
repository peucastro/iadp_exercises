import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

# Print the values from columns 'Invoice ID' and 'Total' from row 0 and 2.


def solve():
    print(df.loc[[0, 2], ["Invoice ID", "Total"]])


solve()
