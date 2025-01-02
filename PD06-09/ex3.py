import pandas as pd

df = pd.read_csv(
    "gym2_q1.csv", sep=";", index_col="id", parse_dates=["date"], dayfirst=True
)

# Create a table with the number of customers by status and sex registered after 2014.


def solve():
    a = df.loc[df["date"].dt.year > 2014]
    df_gym = a.pivot_table(index="status", columns="sex", aggfunc="size")
    print(df_gym)


solve()
