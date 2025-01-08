import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

# Print the bottom three values of the number of birthdays per year.


def solve():
    print(df["birthday"].dt.year.value_counts().sort_values(ascending=False).tail(3))


solve()
