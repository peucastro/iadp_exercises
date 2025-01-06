import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

# Print the values from columns 'race' to 'salary' from rows 1, 4, and 6.


def solve():
    print(df.loc[[1, 4, 6], "race":"salary"])


solve()
