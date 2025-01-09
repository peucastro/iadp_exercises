import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# Delete the rows from the dataframe where 'Payment_Method' is equal to 'Credit Card'.


def solve():
    aux = df.loc[df["Payment_Method"] == "Credit Card"].index
    df.drop(aux, inplace=True)


print(df.shape)
solve()
print(df.shape)
print(df.loc[:, "Final_Price":"Purchase_Date"].head(3))
