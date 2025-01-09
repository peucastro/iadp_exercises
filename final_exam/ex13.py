import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# Calculate for 'Category' the mean of the 'Price' sorted in descending order (rounded to two decimal place).


def solve():
    print(
        df.groupby("Category")["Price"]
        .agg("mean")
        .sort_values(ascending=False)
        .round(2)
    )


solve()
