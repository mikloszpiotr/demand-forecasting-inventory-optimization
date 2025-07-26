import pandas as pd
from scipy.stats import norm

def calculate_kpis(forecast_df, lead_time=3, service_level=0.975, holding_cost=2, ordering_cost=50):
    """
    Calculate Inventory KPIs: Avg Forecast, Safety Stock, Reorder Point, EOQ.

    Parameters:
    - forecast_df: DataFrame with columns ['product_id', 'forecast']
    - lead_time: Lead time in days (default: 3)
    - service_level: Desired service level (default: 97.5%)
    - holding_cost: Annual holding cost per unit
    - ordering_cost: Fixed cost per order

    Returns:
    - DataFrame with KPIs per product_id
    """
    z = norm.ppf(service_level)

    results = []
    for product_id, group in forecast_df.groupby("product_id"):
        avg_forecast = group["forecast"].mean()
        std_forecast = group["forecast"].std()

        safety_stock = round(z * std_forecast * (lead_time ** 0.5))
        reorder_point = round(avg_forecast * lead_time + safety_stock)
        annual_demand = avg_forecast * 365
        eoq = round(((2 * annual_demand * ordering_cost) / holding_cost) ** 0.5)

        results.append({
            "product_id": product_id,
            "Avg Forecast": round(avg_forecast),
            "Lead Time": lead_time,
            "Safety Stock": safety_stock,
            "Reorder Point": reorder_point,
            "EOQ": eoq
        })

    return pd.DataFrame(results)
