import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
import warnings

# Setup
warnings.filterwarnings("ignore")
sns.set(style="whitegrid")

# Streamlit app
st.title("Retail Sales Analysis Dashboard")
st.write("Explore sales trends, top products, and forecasts using retail sales data.")

# Load data
try:
    df = pd.read_csv(
        "C:/Users/user/Documents/retail-sales-analysis/data/retail_sales.csv"
    )
    df["Date"] = pd.to_datetime(df["Date"])
    st.write("Data loaded successfully")
except FileNotFoundError:
    st.error("Error: retail_sales.csv not found in data/")
    st.stop()

# Sidebar filters
st.sidebar.header("Filters")
category = st.sidebar.multiselect(
    "Product Category",
    options=df["Product Category"].unique(),
    default=df["Product Category"].unique(),
)
start_date = st.sidebar.date_input("Start Date", df["Date"].min())
end_date = st.sidebar.date_input("End Date", df["Date"].max())

# Filter data
filtered_df = df[
    df["Product Category"].isin(category)
    & (df["Date"] >= pd.to_datetime(start_date))
    & (df["Date"] <= pd.to_datetime(end_date))
]

# Sales trend
st.subheader("Monthly Sales Trend")
monthly_sales = filtered_df.groupby(filtered_df["Date"].dt.to_period("M"))[
    "Total Amount"
].sum()
fig, ax = plt.subplots(figsize=(10, 6))
monthly_sales.plot(ax=ax)
ax.set_title("Monthly Sales Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

# Top products
st.subheader("Top Product Categories")
top_products = (
    filtered_df.groupby("Product Category")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_products.values, y=top_products.index, ax=ax)
ax.set_title("Top Product Categories by Sales")
ax.set_xlabel("Total Sales ($)")
ax.set_ylabel("Product Category")
plt.tight_layout()
st.pyplot(fig)

# Sales forecast
st.subheader("Sales Forecast (12 Months)")
monthly_sales_ts = monthly_sales.to_timestamp()
try:
    model = ARIMA(monthly_sales_ts, order=(1, 1, 1))
    results = model.fit()
    forecast = results.forecast(steps=12)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(monthly_sales_ts, label="Historical Sales")
    ax.plot(forecast, label="Forecast", color="red")
    ax.set_title("Sales Forecast (12 Months)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Sales ($)")
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)
except Exception as e:
    st.write("Forecasting not available for filtered data")

# Display sample data
st.subheader("Sample Data")
st.dataframe(filtered_df[["Date", "Product Category", "Total Amount"]].head())
