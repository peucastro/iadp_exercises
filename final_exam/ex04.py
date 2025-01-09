import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# What is the Product_ID having the highest 'Price' (rounded to one decimal place).


def solve():
    aux = df.sort_values("Price", ascending=False)
    print(f"Product_ID: {aux.iloc[0].Product_ID}")
    print(f"Price: {aux.iloc[0].Price:.1f}")


solve()
