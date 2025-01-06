import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

# Calculate the minimum, maximum and the median of the 'age' for the persons with a 'salary' greater than or equal 150000 (rounded to one decimal place)


def solve():
    aux = df.loc[df["salary"] >= 150000]
    age_stats = aux["age"].agg(["min", "max", "median"]).round(2)
    print(age_stats)


solve()
