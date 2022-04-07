from finances.src import app
from finances.src import config

app.configuration = config.Configuration(
    binance_key_public="Yiux33U9VQCjdAr9R10HurLLasClPCyKFrKAAmghh7koEDE6XCvd6AWGQJl0D8pp",
    binance_key_private="ejpcwWp7vXTJ8XGb8GGtlg7Kukz2z8wmtzPMqtdSXRAnhddAYqLykhkmPnGrGKGG",
    fav_stocks=["ibm, hpe, btc-usd"],
    fav_leading_index="^gdaxi"
)


def test_crypto():
    assert app.crypto() is not None


def test_favourites():
    assert app.favourites() is not None


def test_leading():
    assert app.leading() is not None

def test_wallstreetbets():
    assert app.wallstreetbets() is not None


def test_nft():
    assert app.nft() is not None


def test_ticker_info():
    assert app.ticker_info("ibm") is not None
