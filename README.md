# Retail Sales Analysis

This project analyzes retail sales data to identify trends, top-selling products, and forecast future sales. Includes exploratory data analysis, visualizations, and an interactive Streamlit app.

## Features

- Exploratory data analysis (EDA) on sales trends and product categories.
- Visualizations: monthly sales trends, top products, and sales forecasts.
- Sales forecasting using ARIMA.
- Interactive Streamlit dashboard for filtering and exploring data.
- Automated Python script for analysis pipeline.

## Setup

1. Clone the repository:
   git clone https://github.com/arlertwebservices/retailsalesanalysis.git

2. Install dependencies:pip install -r requirements.txt

3. Download the dataset:
   Get retail_sales_dataset.csv from Kaggle.
   Place it in data/retail_sales.csv.

4. Run the notebook:
   jupyter notebook notebooks/analysis.ipynb

5. Run the script:
   python src/analysis.py

6. Run the Streamlit app:
   streamlit run src/app.py

Folder Structure
retail-sales-analysis/
├── data/
│ ├── retail_sales.csv
│ ├── processed_sales.csv
├── notebooks/
│ ├── analysis.ipynb
├── src/
│ ├── analysis.py
│ ├── app.py
├── figures/
│ ├── sales_trend.png
│ ├── top_products.png
│ ├── sales_forecast.png
├── .env
├── README.md
├── requirements.txt
├── .gitignore

License
MIT
