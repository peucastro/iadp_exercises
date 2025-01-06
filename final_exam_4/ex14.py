import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

# Print the 'status', the 'race' and the value corresponding to the highest mean 'age' (rounded to one decimal place) by 'status' and 'race'.


def solve():
    aux = df.groupby(["status", "race"])["age"].mean().round(1)
    aux = aux.sort_values(ascending=False)
    idx = aux.idxmax()
    print(f"{idx[0]}, {idx[1]}, {aux.max()}")


solve()
