# 📦 Demand Forecasting & Inventory Optimization

This repository presents an end-to-end **machine learning solution** tailored for supply chain professionals. It addresses a common challenge in demand planning: how to **accurately forecast product demand** and use that insight to **optimize inventory levels** — minimizing stockouts and excess while improving service levels.

---

## 🎯 Business Problem

**Real-world Challenge**  
Demand planners and supply chain managers often rely on manual forecasts or spreadsheets. These can’t effectively respond to:
- Promotion periods
- Seasonal changes
- Lead time variability

**Business Impact**  
- ⛔ Stockouts → missed sales
- 💸 Overstock → wasted cash and warehouse space
- 😐 Poor service levels → lost customers

---

## ✅ Project Objective

This project uses **machine learning + interactive dashboards** to:

- Predict future demand for individual products
- Quantify inventory needs based on that forecast
- Recommend Safety Stock, Reorder Point, and EOQ
- Visualize and export predictions for decision-making

---

## 🧩 Who Should Use This?

- 📊 **Demand Planners**
- 🧠 **Supply Chain Data Analysts**
- 🏭 **Inventory Managers**
- 🤖 **ML Engineers in Operations or Logistics**

---

## 📈 Project Highlights

| Module                | What it Does                                        |
|-----------------------|-----------------------------------------------------|
| `app.py`              | Launches a Streamlit dashboard for business users   |
| `data/`               | Contains raw sales, calendar, and product files     |
| `models/`             | Trained ML model (XGBoost) for demand forecasting   |
| `src/`                | Scripts for data loading, cleaning, features, model |
| `notebooks/`          | Full EDA: trends, seasonality, promotions, outliers |
| `README.md`           | Professional documentation                          |

---

## 🧠 ML Pipeline Overview

### 1. 📌 Problem Definition
- **Task**: Regression – forecast daily product-level demand
- **Success Metrics**: MAE, Forecast Bias, Inventory ROI

### 2. 🧾 Data Collection
- Synthetic historical data with 3 datasets:
  - `sales_data.csv`
  - `product_master.csv`
  - `calendar.csv` (promo/holiday flags)

---

### 🔍 3. Exploratory Data Analysis (EDA)

Conducted in `notebooks/01_eda_full.ipynb` using Seaborn and Matplotlib:

- 📈 Sales trends over time (daily/weekly)
- 🔁 Seasonality and cyclic patterns
- 🛍️ Promo vs non-promo analysis
- 📅 Heatmaps for weekday and month-level demand
- ⭐ Top-selling products overview

---

### 🧼 4. Data Preprocessing

Handled using:
- `src/data/load_data.py`
- `src/data/clean_data.py`

Steps included:
- Merging sales, product, and calendar datasets
- Handling missing promo/holiday indicators
- Removing duplicates
- Filtering invalid records (e.g., negative demand)

---

### 🧱 5. Feature Engineering

Created in `src/features/build_features.py`, including:

- Lag features (e.g., previous day sales)
- Rolling window statistics (7-day mean and std)
- Date-based fields: day of week, month, year
- Promotion and holiday binary flags

---

### 🤖 6. Model Training
- Algorithm: **XGBoost Regressor**
- Trained on 1 year of filtered data (for fast app load)
- Model file: `xgb_model.pkl`

Script: `src/models/train_model.py`

---

### 💻 7. Streamlit App
- Forecast chart: actual vs predicted
- KPIs: EOQ, Safety Stock, Reorder Point
- Export: download forecast as `.csv`

---

## 🚀 How to Run

1. Clone this repo:
```bash
git clone https://github.com/mikloszpiotr/demand-forecasting-inventory-optimization.git
cd demand-forecasting-inventory-optimization
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch the dashboard:
```bash
streamlit run app.py
```

---

## 📊 Portfolio Focus

This project was built as part of my **Supply Chain ML Portfolio**, with a focus on:
- Clean modular structure
- Reusable data pipeline
- Business-focused metrics & dashboard
- Realistic use cases that can be adapted for SAP / ERP integration

---

## 👨‍💼 Author

**Piotr Miklosz**  
Data-Driven Supply Chain Analyst  
🔗 [GitHub](https://github.com/mikloszpiotr)

---

## 🏁 Next Projects

- 📍 Project 2: Delivery Time Classification & Dynamic Routing  
- 📍 Project 3: Anomaly Detection in Warehouse Operations
