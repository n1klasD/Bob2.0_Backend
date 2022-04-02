import sys

from binance import Client
from yahoo_fin.stock_info import get_quote_data

sys.path.append("../TradeRepublicApi")
from trapi.api import TRApi


def get_binance_info():
    api_key = "Yiux33U9VQCjdAr9R10HurLLasClPCyKFrKAAmghh7koEDE6XCvd6AWGQJl0D8pp"
    api_secret = ""  # TODO add key
    client = Client(api_key, api_secret)
    info = client.get_account()
    return info["balances"]


async def get_tr_info():
    NUMBER = ""  # TODO
    PIN = ""  # TODO
    tr = TRApi(NUMBER, PIN)
    tr.login()
    portfolio = None

    def set_portfolio(portfolio_json):
        nonlocal portfolio
        portfolio = portfolio_json

    await tr.portfolio(callback=set_portfolio)
    await tr.start()

    return portfolio


def ticker_info(ticker: str) -> tuple[str, str, float]:
    info = get_quote_data(ticker)
    return info["shortName"], info["regularMarketPrice"], info["currency"]
