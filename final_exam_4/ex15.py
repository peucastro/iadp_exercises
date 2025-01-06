import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

# Calculate the average salary for 'status': 'Never-married' and 'Married-civ-spouse' for 'race' 'White' (rounded to one decimal place).


def solve():
    aux = df.loc[
        ((df["status"] == "Never-married") | (df["status"] == "Married-civ-spouse"))
        & (df["race"] == "White")
    ]
    print(
        aux.pivot_table(index="status", columns="race", values="salary", aggfunc="mean").round(1)
    )


solve()
