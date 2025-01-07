import pandas as pd

df = pd.read_csv("f1_1.csv", encoding="utf-8", parse_dates=["dob", "date"])

# Insert a column named 'surname' before column 'dob' with the driver's surname. (assume the surname is the last word in the full name)


def solve():
    surnames = df["name"].str.split().str[-1]
    df.insert(2, "surname", surnames)


solve()
print(df.head(3))
