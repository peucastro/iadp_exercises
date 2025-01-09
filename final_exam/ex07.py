import pandas as pd

df = pd.read_csv("ecommerce1.csv", parse_dates=["Purchase_Date"])
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

"""
Create a function 'convert(string)' that, given a string returns a new string with the first letter of the first and last words. If the string has only one word, the function should return the first two letters of the word. Create a function 'solve()' that, using the function 'convert(string)', converts the column 'Payment_Method'.
"""


def convert(string):
    words = string.split(" ")
    if len(words) == 1:
        return string[0:2]

    size = len(words)
    return words[0][0] + words[size - 1][0]


def solve():
    df["Payment_Method"] = df["Payment_Method"].apply(convert)


print(convert("One Test"))
solve()
print(df["Payment_Method"].unique())
