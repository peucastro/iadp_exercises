import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

# Calculate the mean of the Invoice 'Total' for Female customers. (rounded to one decimal place)


def solve():
    print(df.loc[(df["Gender"] == "Female"), ["Total"]].mean().round(1))


solve()
