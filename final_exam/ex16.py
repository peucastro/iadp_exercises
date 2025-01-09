import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# Print the 'Category' and the 'Payment_Method' with the highest total of 'Final_Price' (sum of the 'Price' for each 'Category' and 'Payment_Method').


def solve():
    grouped = df.groupby(["Category", "Payment_Method"])["Final_Price"].sum().idxmax()
    total_paid = round(
        df.groupby(["Category", "Payment_Method"])["Final_Price"].sum().max()
    )

    print(f"Category: {grouped[0]}")
    print(f"Payment_Method: {grouped[1]}")
    print(f"Total paid: {total_paid}")


solve()
