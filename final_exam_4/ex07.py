import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

# Create a function 'hif_und(name)' that given a string returns a new string replacing the '-' by '_'. Using the 'hif_und(name)' function update the column 'status' replacing the '-' by '_'


def hif_und(name):
    return name.replace("-", "_")


def solve():
    df["status"] = df["status"].apply(hif_und)


print(hif_und("very-high"))
solve()
print(df.loc[:, "age":"status"].head(3))
