import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

# Delete the rows from the dataframe where 'sex' is equal to 'Male' and 'age' greater than or equal 45.


def solve():
    aux = df.loc[(df["sex"] == "Male") & (df["age"] >= 45)].index
    df.drop(aux, inplace=True)


print(df.shape)
solve()
print(df.shape)
solve()
