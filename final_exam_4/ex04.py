import pandas as pd

df = pd.read_csv("adult1.csv", sep=";", parse_dates=["birthday"])

# From the adults having a 'salary' greater than or equal 150000 what is the percentage of married people. Consider as married those who have a 'status' starting with 'Married'. (rounded to one decimal place)


def solve():
    aux = df.loc[df["salary"] >= 150000]
    married_count = aux[aux["status"].str.startswith("Married")].shape[0]
    total_count = aux.shape[0]
    percentage_married = (married_count / total_count) * 100
    print(f"{percentage_married:.1f}%")


solve()
