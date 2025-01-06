import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

# Print the columns 'city' to 'house_size' of the rows where the 'house_size' is greater than 40000.


def solve():
    aux = df.loc[df["house_size"] > 40000]
    print(aux.loc[:, "city":"house_size"])


solve()
