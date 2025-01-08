import pandas as pd

df = pd.read_csv("usa_real_estate1.csv", sep=";", parse_dates=["sold_date"])

# Calculate for each state the 'city' with the highest house 'price'.


def solve():
    pt = df.pivot_table(index="state", columns="city", values="price", aggfunc="max")
    pm = pd.DataFrame(pt.idxmax(axis=1))
    pm["price"] = pt.max(axis=1)
    pm.rename(columns={0: "City"}, inplace=True)
    print(pm)


solve()
