import pandas as pd

df = pd.read_csv("f1_1.csv", encoding="utf-8", parse_dates=["dob", "date"])

# Print the values from columns 'name' to 'points' from rows 3, 5 and 7.


def solve():
    print(df.loc[[3, 5, 7], "name":"points"])


solve()
