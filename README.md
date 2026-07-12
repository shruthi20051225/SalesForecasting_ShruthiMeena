# 📈 End-to-End Sales Forecasting & Demand Intelligence System

## 📌 Project Overview

This project is an end-to-end Sales Forecasting and Demand Intelligence System developed as part of the XYlofy AI Data Science Internship (Week 3 & Week 4).

The system analyzes historical retail sales data, forecasts future demand using multiple forecasting models, detects unusual sales patterns, segments products based on demand, and presents insights through an interactive Streamlit dashboard.

---

## 🎯 Objectives

- Analyze historical retail sales data
- Forecast future sales using multiple forecasting techniques
- Detect unusual sales spikes and drops
- Segment products based on demand behavior
- Build an interactive business dashboard
- Generate actionable business recommendations

---

## 📂 Dataset

### Primary Dataset
- Superstore Sales Dataset (Kaggle)
- File: `train.csv`

### Secondary Dataset
- Video Game Sales Dataset (Kaggle)
- Used for anomaly detection practice

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Statsmodels
- Prophet
- XGBoost
- Scikit-learn
- Streamlit
- Jupyter Notebook
- Git & GitHub

---

## 📊 Project Workflow

### Task 1
- Data Loading
- Data Cleaning
- Feature Engineering
- Time Feature Extraction

### Task 2
- Time Series Analysis
- Monthly Sales Trend
- Seasonal Decomposition
- Stationarity Test (ADF)
- Differencing

### Task 3
Sales Forecasting using:

- SARIMA
- Prophet
- XGBoost

Performance Comparison using:

- MAE
- RMSE
- MAPE

---

### Model Comparison

| Model | MAE | RMSE | MAPE |
|------|------:|------:|------:|
| SARIMA | 6338.47 | 6377.25 | 36.79% |
| Prophet | 12050.66 | 12505.38 | N/A |
| **XGBoost** | **2545.55** | **2722.47** | **14.80%** |

**Best Model:** XGBoost

---

### Task 4

Category & Region Level Forecasting

Forecast generated for:

- Furniture
- Technology
- Office Supplies
- West Region
- East Region

---

### Task 5

Anomaly Detection

Methods Used:

- Isolation Forest
- Z-Score Detection

---

### Task 6

Product Demand Segmentation

K-Means Clustering was applied to group products into:

- High Volume, Stable Demand
- Growing Demand
- Low Volume, High Volatility
- Declining Demand

---

### Task 7

Interactive Streamlit Dashboard

Dashboard Pages:

- 📈 Sales Overview
- 🔮 Forecast Explorer
- 🚨 Anomaly Report
- 📦 Product Demand Segments

---

### Task 8

Executive Business Report

Includes:

- Executive Summary
- Sales Insights
- Forecast Results
- Anomaly Analysis
- Product Segmentation
- Business Recommendations
- Project Limitations

---

## 📁 Project Structure

```
SalesForecasting_ShruthiMeena/
│
├── analysis.ipynb
├── app.py
├── requirements.txt
├── train.csv
├── product_segments.csv
├── summary.docx
├── charts/
│   ├── monthly_sales_trend.png
│   ├── decomposition.png
│   ├── differenced_series.png
│   ├── sarima_forecast.png
│   ├── prophet_forecast.png
│   ├── xgboost_forecast.png
│   ├── category_region_forecast.png
│   ├── isolation_forest_anomalies.png
│   ├── zscore_anomalies.png
│   ├── elbow_method.png
│   └── product_clusters.png
└── README.md
```

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/shruthi20051225/SalesForecasting_ShruthiMeena.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Streamlit Dashboard

```bash
streamlit run app.py
```

---

## 📈 Results

- Successfully analyzed four years of retail sales data.
- Built three forecasting models.
- XGBoost achieved the best forecasting performance.
- Detected unusual sales events using two anomaly detection techniques.
- Segmented products into meaningful demand clusters.
- Developed an interactive Streamlit dashboard for business users.

---

## 📚 Key Business Recommendations

- Maintain higher inventory for high-demand products.
- Use XGBoost forecasts for monthly inventory planning.
- Monitor sales anomalies to quickly identify unusual business events.
- Increase inventory for growing-demand products.
- Optimize stock levels based on demand segmentation.

---

## 👩‍💻 Author

**Shruthi Meena**

Data Science Intern – XYlofy AI

GitHub: https://github.com/shruthi20051225

---

## ⭐ Acknowledgements

- XYlofy AI Internship Program
- Kaggle Datasets
- Open-source Python Community
- Streamlit
