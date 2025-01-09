import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# What is the 'Payment_Mehod' having the maximum total amount paid (sum of the 'Final_Price') (rounded to two decimal places).


def solve():
    aux = df.pivot_table(
        index="Payment_Method", values="Final_Price", aggfunc="sum"
    ).sort_values("Final_Price", ascending=False)
    print(f"Payment_Method: {aux.iloc[0].name}")
    print(f"value: {aux.iloc[0].Final_Price:.2f}")


solve()
