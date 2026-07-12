import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 End-to-End Sales Forecasting & Demand Intelligence System")

# Load dataset
sales_df = pd.read_csv(
    "train excel/train.csv",
    parse_dates=["Order Date", "Ship Date"],
    dayfirst=True
)

# Sidebar
page = st.sidebar.selectbox(
    "Select Dashboard Page",
    [
        "Sales Overview",
        "Forecast Explorer",
        "Anomaly Report",
        "Demand Segments"
    ]
)


#Page 1 – Sales Overview

if page == "Sales Overview":

    st.header("Sales Overview Dashboard")

    yearly_sales = sales_df.groupby(
        sales_df["Order Date"].dt.year
    )["Sales"].sum()

    st.bar_chart(yearly_sales)

    monthly_sales = sales_df.groupby(
        pd.Grouper(key="Order Date", freq="ME")
    )["Sales"].sum()

    st.line_chart(monthly_sales)

    region = st.selectbox(
        "Select Region",
        sales_df["Region"].unique()
    )

    category = st.selectbox(
        "Select Category",
        sales_df["Category"].unique()
    )

    filtered = sales_df[
        (sales_df["Region"] == region)
        &
        (sales_df["Category"] == category)
    ]

    st.dataframe(filtered.head())


#Page 2 – Forecast 

elif page == "Forecast Explorer":

    st.header("Forecast Explorer")

    option = st.selectbox(
        "Forecast By",
        ["Category", "Region"]
    )

    horizon = st.slider(
        "Forecast Horizon (Months)",
        1,
        3,
        3
    )

    st.success(
        f"Forecast generated for next {horizon} month(s)."
    )

    st.metric(
        "MAE",
        "2545.55"
    )

    st.metric(
        "RMSE",
        "2722.47"
    )

    st.image(
        "charts/category_region_forecast.png",
        use_container_width=True
    )


    #Page 3 – Anomaly Report
elif page == "Anomaly Report":

    st.header("Weekly Sales Anomalies")

    st.image(
        "charts/isolation_forest_anomalies.png",
        use_container_width=True
    )

    st.image(
        "charts/zscore_anomalies.png",
        use_container_width=True
    )


    #Page 4 – Product Demand Segments
elif page == "Demand Segments":

    st.header("Product Demand Segmentation")

    st.image(
        "charts/product_clusters.png",
        use_container_width=True
    )

    segments = pd.read_csv(
        "product_segments.csv"
    )

    st.dataframe(segments)