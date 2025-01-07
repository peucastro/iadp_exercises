import pandas as pd

df = pd.read_csv("f1_1.csv", encoding="utf-8", parse_dates=["dob", "date"])

# Delete the rows corresponding to the driver 'Lewis Hamilton'.


def solve():
    aux = df.loc[df["name"] == "Lewis Hamilton"].index
    df.drop(aux, inplace=True)


print(df.shape)
solve()
print(df.shape)
