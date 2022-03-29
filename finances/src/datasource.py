from binance import Client
from yahoo_fin.stock_info import get_quote_data


def get_binance_info():
    api_key = "Yiux33U9VQCjdAr9R10HurLLasClPCyKFrKAAmghh7koEDE6XCvd6AWGQJl0D8pp"
    api_secret = ""  # TODO add key
    client = Client(api_key, api_secret)
    info = client.get_account()
    return info["balances"]


def ticker_info(ticker: str) -> tuple[str, str, float]:
    info = get_quote_data(ticker)
    return info["shortName"], info["regularMarketPrice"], info["currency"]
