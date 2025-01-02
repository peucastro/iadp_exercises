import pandas as pd

df = pd.read_csv("gym_q1.csv", sep=";", index_col="id", parse_dates=["date"])

# Create a table with the number of customers by status and sex registered after 2014.


def solve():
    df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")
    filtered_df = df[df["date"].dt.year > 2014]
    pivot = filtered_df.pivot_table(index="status", columns="sex", aggfunc="size")
    print(pivot)


solve()
