from flask import Flask

from finances.src import datasource

app = Flask(__name__)


@app.route('/stocks')
def stocks():
    pass


@app.route('/crypto')
def crypto():
    balances = datasource.get_binance_info()
    balances_not_null = []

    for balance in balances:
        if float(balance["free"]) != 0:
            balances_not_null.append(f" {balance['asset']}:\t{balance['free']} \n")

    if balances_not_null:
        return "Deine Kryptos aktuell: " + "\n".join(balances_not_null)

    return "Du hast aktuell keine Kryptos."


@app.route('/all')
def all_investments():
    pass


@app.route('/info/<ticker>')
def dj(ticker):
    try:
        name, value, currency = datasource.ticker_info(ticker)
        return f"{name} liegt aktuell bei {value:.2f} {currency}."
    except Exception as e:
        print(e)
        return "Die Daten für dieses Kürzel konnten nicht abgerufen werden."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
