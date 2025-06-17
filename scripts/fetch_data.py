import pandas as pd
import requests

def get_tiingo_data(ticker, start_date, end_date, api_key):
    url = (
        f"https://api.tiingo.com/tiingo/daily/{ticker}/prices"
        f"?startDate={start_date}&endDate={end_date}&format=csv&token={api_key}"
    )
    df = pd.read_csv(url, parse_dates=["date"])
    df = df.rename(columns={"date": "Date", "adjClose": "Adj Close"}).set_index("Date")
    return df.sort_index()
