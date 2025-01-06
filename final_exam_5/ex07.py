import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

# Insert a column named 'price_euros' before column 'bed' converting the value in dollars from column 'price' to euros (1 Dollar = 0.95 Euro) (rounded to one decimal place)


def solve():
    df.insert(2, "price_euros", (df["price"] * 0.95).round(1))


solve()
print(df.head(3))
