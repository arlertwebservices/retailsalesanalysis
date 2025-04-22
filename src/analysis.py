import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
import warnings


def load_data():
    """Load and preprocess sales data."""
    try:
        df = pd.read_csv(
            "C:/Users/user/Documents/retail-sales-analysis/data/retail_sales.csv"
        )
        df["Date"] = pd.to_datetime(df["Date"])
        print("Data loaded and Date converted")
        return df
    except FileNotFoundError:
        print("Error: retail_sales.csv not found")
        raise


def perform_eda(df):
    """Perform exploratory data analysis."""
    print("Dataset Info:")
    print(df.info())
    print("\nSummary Statistics:")
    print(df.describe())
    print("\nMissing Values:")
    print(df.isnull().sum())
    category_sales = (
        df.groupby("Product Category")["Total Amount"]
        .sum()
        .sort_values(ascending=False)
    )
    print("\nSales by Category:")
    print(category_sales)
    return category_sales


def plot_sales_trend(df):
    """Plot monthly sales trend."""
    monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Total Amount"].sum()
    plt.figure(figsize=(10, 6))
    monthly_sales.plot()
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("C:/Users/user/Documents/retail-sales-analysis/figures/sales_trend.png")
    plt.close()
    print("Sales trend plot saved")
    return monthly_sales


def plot_top_products(df):
    """Plot top product categories by sales."""
    top_products = (
        df.groupby("Product Category")["Total Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_products.values, y=top_products.index)
    plt.title("Top Product Categories by Sales")
    plt.xlabel("Total Sales ($)")
    plt.ylabel("Product Category")
    plt.tight_layout()
    plt.savefig(
        "C:/Users/user/Documents/retail-sales-analysis/figures/top_products.png"
    )
    plt.close()
    print("Top products plot saved")


def forecast_sales(monthly_sales):
    """Forecast sales using ARIMA."""
    monthly_sales_ts = monthly_sales.to_timestamp()
    model = ARIMA(monthly_sales_ts, order=(1, 1, 1))
    results = model.fit()
    forecast = results.forecast(steps=12)
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_sales_ts, label="Historical Sales")
    plt.plot(forecast, label="Forecast", color="red")
    plt.title("Sales Forecast (12 Months)")
    plt.xlabel("Date")
    plt.ylabel("Total Sales ($)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(
        "C:/Users/user/Documents/retail-sales-analysis/figures/sales_forecast.png"
    )
    plt.close()
    print("Sales forecast plot saved")


def save_processed_data(df):
    """Save processed data."""
    df.to_csv(
        "C:/Users/user/Documents/retail-sales-analysis/data/processed_sales.csv",
        index=False,
    )
    print("Processed data saved")


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    sns.set(style="whitegrid")
    df = load_data()
    category_sales = perform_eda(df)
    monthly_sales = plot_sales_trend(df)
    plot_top_products(df)
    forecast_sales(monthly_sales)
    save_processed_data(df)
