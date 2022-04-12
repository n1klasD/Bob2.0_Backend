import requests
from binance import Client
from bs4 import BeautifulSoup
from yahoo_fin.stock_info import get_quote_data, get_day_gainers


class datasources:
    @staticmethod
    def get_binance_info(key_public, key_private):
        client = Client(key_public, key_private)
        info = client.get_account()
        return info["balances"]

    @staticmethod
    def get_ticker_info(ticker):
        info = get_quote_data(ticker)
        return info["shortName"], info["regularMarketPrice"], info["currency"]

    @staticmethod
    def get_top_3_day_gainers():
        return get_day_gainers(3)

    @staticmethod
    def get_most_discussed_stock():
        top_50 = requests.get("https://tradestie.com/api/v1/apps/reddit").json()
        return top_50[0]

    @staticmethod
    def get_top_nft():
        nft_stats = requests.get("https://www.nft-stats.com/top-sales/24h").content
        soup = BeautifulSoup(nft_stats, 'html.parser')

        table = soup.find("table", {"class": "table table-sm"})
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')

        top_nft_row = rows[1]

        cols = top_nft_row.find_all('td')

        name = cols[1].find("a").text
        collection = cols[2].find("a").text
        hours_ago = cols[3].text.split(" ")[1]
        value = cols[4].text

        return name, collection, hours_ago, value
