import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# In what month do people make more purchases.


def solve():
    aux = df["Purchase_Date"].dt.month
    month_purchases = aux.value_counts().idxmax()
    num_purchases = aux.value_counts().max()
    print(f"Month: {month_purchases}")
    print(f"Number of purchases: {num_purchases}")


solve()
