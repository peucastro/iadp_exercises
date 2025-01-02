import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

# Delete the rows corresponding to 'City' 'Yangon'.


def solve():
    df_yangon = df.loc[(df["City"] == "Yangon")].index
    df.drop(df_yangon, inplace=True)


solve()
