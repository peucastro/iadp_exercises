import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

# How many people earn more than 150000. Of those people how many have an 'education' greater than or equal to 13.


def solve():
    aux = df.loc[df["salary"] > 150000]
    print(aux.shape[0])
    aux = aux.loc[aux["education"] >= 13]
    print(aux.shape[0])


solve()
