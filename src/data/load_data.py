import pandas as pd
import os

def load_data(data_path="../data/raw"):
    sales = pd.read_csv(os.path.join(data_path, "sales_data.csv"), parse_dates=["date"])
    product = pd.read_csv(os.path.join(data_path, "product_master.csv"))
    calendar = pd.read_csv(os.path.join(data_path, "calendar.csv"), parse_dates=["date"])
    return sales, product, calendar
