from flask import Flask, request

from finances.src import datasource, config

app = Flask(__name__)


@app.route("/crypto")
def crypto():
    balances = datasource.get_binance_info(configuration.binance_key_public, configuration.binance_key_private)
    balances_not_null = []

    for balance in balances:
        if float(balance["free"]) != 0:
            balances_not_null.append(f" {balance['asset']}:\t{balance['free']} \n")

    if balances_not_null:
        return "Deine Kryptos aktuell:\n" + "\n".join(balances_not_null)

    return "Du hast aktuell keine Kryptos.\n"


@app.route("/favourites")
def favourites():
    answer = "Deine Favoriten: \n"
    for ticker in configuration.fav_stocks:
        answer += ticker_info(ticker)

    return answer


@app.route("/leading")
def leading():
    answer = "Dein favorisierter Leitindex: \n"
    answer += ticker_info(configuration.fav_leading_index)
    return answer


@app.route("/settings", methods=['POST'])
def settings():
    data = request.get_json()
    configuration.binance_key_private = data["binance_key_private"]
    configuration.binance_key_public = data["binance_key_public"]
    configuration.fav_stocks = data["fav_stocks"]
    configuration.fav_leading_index = data["fav_leading_index"]


@app.route("/wallstreetbets")
def wallstreetbets():
    try:
        most_discussed = datasource.get_most_discussed_stock()
        name, value, currency = datasource.get_ticker_info(most_discussed["ticker"])

        return f"Auf r/wallstreetbets wird heute {name} mit {most_discussed['no_of_comments']} Kommentaren als {most_discussed['sentiment']} angesehen. " \
               f"Der aktuelle Wert liegt bei  {value} {currency}. \n"
    except Exception as e:
        print(e)
        return "Wallstreetbets kann gerade nicht abgerufen werden"


@app.route("/nft")
def nft():
    try:
        name, collection, hours_ago, value = datasource.get_top_nft()
        return f"{name} aus der Kollektion {collection} wurde vor {hours_ago} Stunden für {value} verkauft.\n"
    except Exception as e:
        print(e)
        return "NFT Informationen können gerade nicht abgerufen werden.\n"


@app.route("/info/<ticker>")
def ticker_info(ticker):
    try:
        name, value, currency = datasource.get_ticker_info(ticker)
        return f"{name} liegt aktuell bei {value:.2f} {currency}. \n"
    except Exception as e:
        print(e)
        return "Die Daten für dieses Kürzel konnten nicht abgerufen werden.\n"


if __name__ == "__main__":
    configuration = config.Configuration(
        binance_key_public="Yiux33U9VQCjdAr9R10HurLLasClPCyKFrKAAmghh7koEDE6XCvd6AWGQJl0D8pp",
        binance_key_private="ejpcwWp7vXTJ8XGb8GGtlg7Kukz2z8wmtzPMqtdSXRAnhddAYqLykhkmPnGrGKGG",
        fav_stocks=["ibm", "hpe", "btc-usd"],
        fav_leading_index="^gdaxi"
    )

    app.run(host="0.0.0.0", port=8000, debug=True)
