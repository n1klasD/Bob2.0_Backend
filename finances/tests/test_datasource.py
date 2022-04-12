from mock import patch

from finances.src import datasource


def test_binance():
    class CustomClient:
        def __init__(self):
            self.data = {
                "balances": [
                    {
                        "free": 0,
                        "asset": "btc"
                    },
                    {
                        "free": 1,
                        "asset": "eth"
                    }
                ]
            }

        def get_account(self):
            return self.data

    with patch("finances.src.datasource.Client") as patched_Client:
        patched_Client.return_value = CustomClient()

        balances = datasource.get_binance_info("a", "b")
        assert balances[0]["free"] == 0 and \
               balances[0]["asset"] == "btc" and \
               balances[1]["free"] == 1 and \
               balances[1]["asset"] == "eth"


def test_day_gainers():
    with patch("finances.src.datasource.get_day_gainers") as patched_get_day_gainers:
        patched_get_day_gainers.return_value = [1, 2, 3]

        assert datasource.get_top_3_day_gainers() == [1, 2, 3]


def test_yahoo():
    with patch("finances.src.datasource.get_quote_data") as patched_get_quote_data:
        patched_get_quote_data.return_value = {"shortName": "IBM", "regularMarketPrice": 4000.00, "currency": "USD"}

        name, value, currency = datasource.get_ticker_info("ibm")

        assert name == "IBM" and value == 4000.00 and currency == "USD"


def test_nft():
    class CustomResponse:
        def __init__(self, content):
            self.content = content

    with patch("finances.src.datasource.requests.get") as patched_get:
        patched_get.return_value = CustomResponse("""
        <table class="table table-sm">
            <tbody>
                <tr></tr>
                <tr>
                    <td></td>
                    <td> <a>nft</a> </td>
                    <td> <a>collection</a> </td>
                    <td>about 22 hours ago</td>
                    <td>4500$</td>
                </tr>
            </tbody>
        </table>
        """)

        name, collection, hours_ago, value = datasource.get_top_nft()

        assert name == "nft" and collection == "collection" and hours_ago == "22" and value == "4500$"


def test_wallstreetbets():
    class CustomResponse:
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return [self.json_data, ]

    with patch("finances.src.datasource.requests.get") as patched_get:
        patched_get.return_value = CustomResponse({
            "sentiment": "Bullish",
            "no_of_comments": 128
        })

        most_discussed = datasource.get_most_discussed_stock()

        assert most_discussed["sentiment"] == "Bullish" and most_discussed["no_of_comments"] == 128
