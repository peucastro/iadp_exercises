import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

"""
Create a function solve() that returns a dataframe with the columns 'Category' to 'Final_Price' of the rows where
the 'Category' is equal to 'Sports' and the 'Price' is greater than 200
or
the 'Category' is 'Clothing' and the 'Price' is less than 200.
"""


def solve():
    return df.loc[
        ((df["Category"] == "Sports") & (df["Price"] > 200))
        | ((df["Category"] == "Clothing") & (df["Price"] < 200)),
        "Category":"Final_Price",
    ]


df1 = solve()
print(df1.head(3))
