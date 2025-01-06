import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

# Delete the rows where the 'price' is greater than 800000.


def solve():
    aux = df.loc[df["price"] > 800000].index
    df.drop(aux, inplace=True)


print(df.shape)
solve()
print(df.shape)
