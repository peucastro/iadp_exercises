import pandas as pd

df = pd.read_csv("gym2_q1.csv", sep=";", index_col="id", parse_dates=["date"])


def solve():
    aux = df.groupby(["class", "sex"])
    result = aux.agg({"age": "max", "weight": "min", "height": "mean"}).rename(
        columns={"age": "max_age", "weight": "min_weight", "height": "mean_height"}
    )
    result["mean_height"] = result["mean_height"].round(2)
    return result


print(solve())
