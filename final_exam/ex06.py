import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# What is the percentage of rows having 'Price' greater or equal 450 (rounded to one decimal place).


def solve():
    tot = df.shape[0]
    aux = df.loc[df["Price"] >= 450]
    gtr = aux.shape[0]

    print(f"{(gtr / tot * 100):.1f}%")


solve()
