import pandas as pd

def create_features(df):
    df = df.copy()
    df["day_of_week"] = df["date"].dt.dayofweek
    df["week_of_year"] = df["date"].dt.isocalendar().week.astype(int)
    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year
    df["lag_1"] = df.groupby("product_id")["quantity_sold"].shift(1)
    df["rolling_mean_7"] = df.groupby("product_id")["quantity_sold"].shift(1).rolling(window=7).mean()
    df["rolling_std_7"] = df.groupby("product_id")["quantity_sold"].shift(1).rolling(window=7).std()
    df.fillna(0, inplace=True)
    return df
