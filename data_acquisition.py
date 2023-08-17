#Handles fetching and preprocessing historical price data.

import pandas as pd
import pandas_datareader as pdr
from datetime import datetime

# TO_DO : customize the fetch_data() function to handle error cases, additional data sources, or specific data preprocessing steps based on your project's needs.

def fetch_data():
    # Define the stock symbol and date range
    stock_symbol = "AAPL"  # Replace with your desired stock symbol
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 1, 1)
    
    # Fetch the historical price data using pandas_datareader
    try:
        data = pdr.get_data_yahoo(stock_symbol, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    data = fetch_data()
    if data is not None:
        print(data.head())
