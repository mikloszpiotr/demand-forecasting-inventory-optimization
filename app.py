import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os

st.set_page_config(page_title="📦 Demand Forecasting & Inventory Optimization", layout="wide")
st.title("📦 Demand Forecasting & Inventory Optimization")

# Load forecast results
@st.cache_data
def load_forecast_data():
    path = "data/processed/forecast_results.csv"
    return pd.read_csv(path, parse_dates=["date"]) if os.path.exists(path) else pd.DataFrame()

# Load trained model
@st.cache_resource
def load_model():
    path = "models/xgb_model.pkl"
    return joblib.load(path) if os.path.exists(path) else None

df = load_forecast_data()
model = load_model()

st.sidebar.header("Navigation")
section = st.sidebar.radio("Go to:", ["📊 Forecast Explorer", "📈 Inventory KPIs", "⬇️ Export"])

# Forecast Explorer
if section == "📊 Forecast Explorer":
    st.subheader("Forecasted Demand by Product")
    if not df.empty:
        product = st.selectbox("Select Product", df["product_id"].unique())
        temp = df[df["product_id"] == product]
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(temp["date"], temp["actual"], label="Actual", marker="o")
        ax.plot(temp["date"], temp["forecast"], label="Forecast", marker="x")
        ax.set_title(f"Forecast for {product}")
        ax.legend()
        st.pyplot(fig)
    else:
        st.warning("❗ No forecast data found.")

# Inventory KPIs
elif section == "📈 Inventory KPIs":
    st.subheader("Inventory Optimization KPIs")
    if not df.empty:
        avg_demand = df.groupby("product_id")["forecast"].mean()
        lead_times = df.groupby("product_id")["lead_time_days"].first()
        reorder_point = (avg_demand * lead_times).round()
        safety_stock = (avg_demand * 0.5).round()
        eoq = (2 * 1000 * 10 / 1)**0.5  # Sample EOQ formula

        kpi_df = pd.DataFrame({
            "Avg Forecast": avg_demand.round(),
            "Lead Time": lead_times,
            "Safety Stock": safety_stock,
            "Reorder Point": reorder_point,
            "EOQ": round(eoq)
        })
        st.dataframe(kpi_df)
    else:
        st.warning("❗ No data for KPIs.")

# Export Forecast
elif section == "⬇️ Export":
    st.subheader("Download Forecast Results")
    if not df.empty:
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", csv, "forecast_results.csv", "text/csv")
    else:
        st.warning("❗ No data to export.")
