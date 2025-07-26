import pandas as pd

def clean_and_merge(sales, product, calendar):
    df = sales.merge(calendar, on="date", how="left")
    df = df.merge(product, on="product_id", how="left")
    df = df.drop_duplicates()
    df["is_promo"] = df["is_promo"].fillna(0)
    df["is_holiday"] = df["is_holiday"].fillna(0)
    return df
