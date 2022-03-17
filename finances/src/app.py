from datetime import datetime

from flask import Flask

import datasource

app = Flask(__name__)


@app.route('/')
def hello():
    ticker = "ibm"
    date = datetime.strptime("01.01.2022", "%d.%m.%Y")
    # return f"{ticker}: {datasource.stock_price_on_date(ticker, date)}"
    binance_info = datasource.get_binance_info()
    return str(binance_info)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
