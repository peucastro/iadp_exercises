import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# Insert a column named 'Final_Price_VAT' after column 'Final_Price' equal to Final_Price plus VAT tax (23%) (rounded to two decimal places).


def solve():
    df.insert(6, "Final_Price_VAT", (df["Final_Price"] * 1.23).round(2))


solve()
print(df.loc[0:3, "Price":"Payment_Method"])
