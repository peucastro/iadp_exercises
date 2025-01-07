import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

"""
Print the columns 'customer type' to 'Unit price' of the rows where the 'Customer type' is 'Member' and the 'Gender' is 'Male' and the 'Unit price' is greater than 99 or the 'Customer type' is 'Normal' and the 'Gender' is 'Female' and the 'Unit price' is greater than 99
"""


def solve():
    print(
        df.loc[
            (
                (
                    ((df["Customer type"] == "Member") & (df["Gender"] == "Male"))
                    | ((df["Customer type"] == "Normal") & (df["Gender"] == "Female"))
                )
                & (df["Unit price"] > 99)
            ),
            "Customer type":"Unit price",
        ]
    )


solve()
