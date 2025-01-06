import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

# Print the columns 'race' to 'salary' for the rows where the 'salary' is greater than 240000 and race is 'Black'.


def solve():
    aux = df.loc[(df["salary"] > 240000) & (df["race"] == "Black")]
    print(aux.loc[:, "race":"salary"])


solve()
