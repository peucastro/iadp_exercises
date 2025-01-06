import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

# Print the columns 'education' to 'salary' of the rows where the 'education' is greater than 15 and the 'salary' is less than 35000 or the 'education' is less than 5 and the 'salary' is greater than 100000.


def solve():
    aux = df.loc[
        ((df["education"] > 15) & (df["salary"] < 35000))
        | ((df["education"] < 5) & (df["salary"] > 100000))
    ]
    print(aux.loc[:, "education":"salary"])


solve()
