import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# Replace in column 'Category' the word 'Clothing' by 'Clothes'.


def solve():
    df["Category"] = df["Category"].str.replace("Clothing", "Clothes")


print(df[df["Category"].str.contains("Clothing")]["Category"].count())
solve()
print(df[df["Category"].str.contains("Clothes")]["Category"].count())
