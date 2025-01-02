import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

# Calculate the total number of units ('Quantity') sold by 'Product line' and the grand total of units sold.


def solve():
    print(
        df.pivot_table(
            index="Product line",
            values="Quantity",
            aggfunc="sum",
            margins=True,
        )
    )


solve()
