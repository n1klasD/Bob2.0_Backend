import datetime

from binance import Client
from yahoo_fin.stock_info import get_data


def get_binance_info():
    api_key = "fkmprqAUizmipqMw96xnBhCufMej0ti2c42I67Eda8lZWqFHnS23GxU7xabkvW1r"
    api_secret = ""  # TODO add key
    client = Client(api_key, api_secret)
    info = client.get_all_tickers()
    return info


def stock_price_on_date(ticker: str, date: datetime) -> float:
    data = get_data(
        ticker=ticker,
        start_date=date,
        end_date=date + datetime.timedelta(days=1),
        interval="1d"
    )

    return data.Close
