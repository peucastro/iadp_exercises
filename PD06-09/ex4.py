import pandas as pd

df = pd.read_csv("gym2_q1.csv", sep=";", index_col="id", parse_dates=["date"])

# Print a dataframe having for each 'city' the 'class' with the highest number of clients.


def solve():
    aux = df.groupby(["city", "class"]).size().reset_index(name="count")
    result = aux.loc[aux.groupby("city")["count"].idxmax()]
    print(result)


solve()
