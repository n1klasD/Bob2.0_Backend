from finances.src import datasource


def test_binance():
    assert datasource.get_binance_info(
        "Yiux33U9VQCjdAr9R10HurLLasClPCyKFrKAAmghh7koEDE6XCvd6AWGQJl0D8pp",
        "ejpcwWp7vXTJ8XGb8GGtlg7Kukz2z8wmtzPMqtdSXRAnhddAYqLykhkmPnGrGKGG") is not None


def test_yahoo():
    assert datasource.get_ticker_info("ibm") is not None


def test_nft():
    assert datasource.get_top_nft() is not None


def test_wallstreetbets():
    assert datasource.get_most_discussed_stock() is not None
