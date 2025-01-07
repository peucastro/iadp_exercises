import pandas as pd

df = pd.read_csv("f1_1.csv", encoding="utf-8", parse_dates=["dob", "date"])

"""
Find the number of drivers in each of the following number of 'races' classes:
[0, 40[ - novice
[40, 80[ - senior
[80, 120[ - expert
[120, 160[ - star"""


def solve():
    aux = df["name"].value_counts().to_list()
    bins = [0, 40, 80, 120, 160]
    labels = ["novice", "senior", "expert", "star"]
    ans = pd.cut(aux, bins=bins, labels=labels)
    print(ans.value_counts())


solve()
