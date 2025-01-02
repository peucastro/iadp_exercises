import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

# Create a table with the number of invoices by 'City' and 'Customer type' with totals by row and by column.


def solve():
    df_pivot = df.pivot_table(
        index="City",
        columns="Customer type",
        values="Invoice ID",
        aggfunc="count",
        margins=True,
    )
    print(df_pivot)


solve()
