import pandas as pd

df = pd.read_csv("gym2_q1.csv", sep=";", parse_dates=["date"])

# Change the 'rank'  name from old_cat to new_cat and convert the column 'rank' to category dtype.


def solve(old_cat, new_cat):
    df.loc[df["rank"] == old_cat, "rank"] = new_cat
    df["rank"] = df["rank"].astype("category")
    print(df["rank"].cat.categories)


solve("old_category", "new_category")
