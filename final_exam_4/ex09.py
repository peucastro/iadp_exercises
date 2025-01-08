import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

# Insert a column named 'retirementdate' before column 'birthday' equal to the retirement date defined as the day the person turns 66 years old.


def solve():
    df.insert(11, "retirementdate", pd.DateOffset(years=66) + df["birthday"])


solve()
print(df.loc[:, "salary":"birthday"].head(3))
