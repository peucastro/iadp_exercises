import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

# Change in row 2 the 'status' to 'sold' and the 'price' to 60000.


def solve():
    df.loc[2, "status"] = "sold"
    df.loc[2, "price"] = 60000


solve()
print(df.head(3))
