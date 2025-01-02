import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

# Calculate the invoices 'Total' by 'City' and type of 'Payment'. (rounded to two decimal places)


def solve():
    print(
        df.pivot_table(
            index="City", columns="Payment", values="Total", aggfunc="sum"
        ).round(2)
    )


solve()
