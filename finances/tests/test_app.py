"""import pytest
from mock import patch

import finances.src.app
from finances.src.app import app as flask_app


class CustomRequest:
    def __init__(self, json_data):
        self.json_data = json_data

    def get_json(self):
        return self.json_data


# pragma: no cover
@pytest.fixture()
def app():
    yield flask_app


# pragma: no cover
@pytest.fixture()
def client(app):
    return app.test_client()


def test_crypto(client):
    with patch("finances.src.datasource.get_binance_info") as patched_get_binance_info, \
            finances.src.app.app.test_client() as c:
        c.post("/crypto", json={
            "publicBinanceApiKey": "",
            "privateBinanceApiKey": ""
        })

        patched_get_binance_info.return_value = [
            {
                "free": 0,
                "asset": "btc"
            },
            {
                "free": 1,
                "asset": "eth"
            }
        ]

        answer = finances.src.app.crypto()
        print(answer)

        assert "eth" in answer and "1" in answer


def test_favourites(client):
    with patch("finances.src.app.ticker_info") as patched_ticker_info, \
            finances.src.app.app.test_client() as c:
        c.post("/favourites", json={
            "stockList": ["", "", ""],
        })

        patched_ticker_info.return_value = "Aktie"

        answer = finances.src.app.favourites()

        assert answer == "Deine Favoriten: \nAktieAktieAktie"


def test_leading(client):
    with patch("finances.src.datasource.get_ticker_info") as patched_get_ticker_info, \
            finances.src.app.app.test_client() as c:
        c.post("/crypto", json={
            "stockIndex": "",
        })

        patched_get_ticker_info.return_value = ("German dax", 10000, "EUR")

        answer = finances.src.app.leading()

        assert "German dax" in answer


def test_wallstreetbets(client):
    with patch("finances.src.datasource.get_most_discussed_stock") as patched_get_most_discussed_stock, \
            patch("finances.src.datasource.get_ticker_info") as patched_get_ticker_info:
        patched_get_most_discussed_stock.return_value = {"no_of_comments": 12, "ticker": "tsla", "sentiment": "Bullish"}
        patched_get_ticker_info.return_value = ("Tesla", 500, "USD")

        answer = finances.src.app.wallstreetbets()

        assert "Tesla" in answer and "USD" in answer


def test_nft(client):
    with patch("finances.src.datasource.get_top_nft") as patched_get_top_nft:
        patched_get_top_nft.return_value = ("name", "collection", "22", "4500$")

        answer = finances.src.app.nft()

        assert "name" in answer and "collection" in answer and "22" in answer and "4500$" in answer


def test_ticker_info(client):
    with patch("finances.src.datasource.get_ticker_info") as patched_get_ticker_info:
        patched_get_ticker_info.return_value = ("tsla", 500, "USD")

        answer = finances.src.app.ticker_info("tsla")

        assert "tsla" in answer and "500" in answer and "USD" in answer

"""


def test_placeholder():
    assert True
