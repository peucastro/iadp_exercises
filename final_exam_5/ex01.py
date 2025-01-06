import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

# Print the values from columns 'price', 'city' and 'house_size from rows 2 to 5.


def solve():
    print(df.loc[2:5, ["price", "city", "house_size"]])


solve()
