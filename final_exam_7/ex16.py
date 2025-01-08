import pandas as pd

df = pd.read_csv("f1_1.csv", encoding="utf-8", parse_dates=["dob", "date"])

# Print the columns 'name' to 'year' of the rows where the 'year' is equal to 2018 and the 'position' is equal 1 or the 'year' is equal to 2019 and the 'position' is equal to 2.


def solve():
    print(
        df.loc[
            ((df["year"] == 2018) & (df["position"] == 1))
            | ((df["year"] == 2019) & (df["position"] == 2)),
            "name":"year",
        ]
    )


solve()
