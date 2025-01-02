import pandas as pd

df = pd.read_csv("gym2_q1.csv", sep=";", index_col="id", parse_dates=["date"])

# Count the number of participants by class and gender.


def solve():
    df_gym = df.groupby(["class", "sex"])["name"].count()
    print(df_gym)

solve()
