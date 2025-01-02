import pandas as pd

df = pd.read_csv("supermarket1.csv", sep=";")

# Print the 'city', the 'Product line' and the value (rounded to two decimal places) corresponding to the maximum sum of the invoices ('Total') by 'Product line' and 'City'


def solve():
    pivot = df.pivot_table(
        index="City", columns="Product line", values="Total", aggfunc="sum"
    )
    max_value = pivot.max().max()
    city, product_line = pivot.stack().idxmax()
    print(f"{city}, {product_line}, {max_value:.2f}")


solve()
