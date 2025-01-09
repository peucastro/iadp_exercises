import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# Calculate the average of 'Price' (rounded to one decimal place).


def solve():
    print(df["Price"].mean().round(1))


solve()
