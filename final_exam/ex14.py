import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# Print for 'Category' by 'Payment_Method' the total amount paid ('Final_Price') (rounded to two decimal places).


def solve():
    print(
        df.pivot_table(
            index="Category",
            columns="Payment_Method",
            values="Final_Price",
            aggfunc="sum",
        ).round(2)
    )


solve()
