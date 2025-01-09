import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# Print the top three Payment_Methods having more rows.


def solve():
    aux = df["Payment_Method"].value_counts().sort_values(ascending=False).head(3)
    print(aux)


solve()
