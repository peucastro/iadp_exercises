import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# Print the values from columns 'Product_ID', 'Price' and 'Payment_Method' from rows 3 to 5.


def solve():
    print(df.loc[3:5, ["Product_ID", "Price", "Payment_Method"]])


solve()
