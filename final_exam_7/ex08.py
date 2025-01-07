import pandas as pd

df = pd.read_csv("f1_1.csv", encoding="utf-8", parse_dates=["dob", "date"])

# Print the top 5 drivers in number of 'races' (sorted by 'name').


def solve():
    aux = df["name"].value_counts()
    aux = aux.head(5)
    print(aux.sort_index())


solve()
