import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

# What is the minimum 'age' and what is the average 'salary' for people with that 'age'. (rounded to one decimal place)


def solve():
    min_age = df["age"].min()
    aux = df.loc[df["age"] == min_age]
    avg_salary = aux["salary"].mean().round(1)
    print(f"Minimum age: {min_age}")
    print(f"Average salary for people with that age: {avg_salary}")


solve()
