from flask import Flask, request

from .datasource import datasources

app = Flask(__name__)


@app.route("/briefing", methods=['POST'])
def briefing():
    answer = "Dein tägliches Finanz-Update.\n\nDay Gainers:\n"

    day_gainers = datasources.get_top_3_day_gainers()
    for _, day_gainer in day_gainers.iterrows():
        name, _, _ = datasources.get_ticker_info(day_gainer.Symbol)
        answer += f"{name} ist ein Gainer mit {day_gainer['% Change']} % Zunahme.\n"

    answer += "\n" + favourites(1)
    answer += "\n" + leading()

    return answer


@app.route("/crypto", methods=['POST'])
def crypto():
    data = request.get_json()
    public_binance_api_key = data["publicBinanceApiKey"]
    private_binance_api_key = data["privateBinanceApiKey"]

    balances = datasources.get_binance_info(public_binance_api_key, private_binance_api_key)
    balances_not_null = []

    for balance in balances:
        if float(balance["free"]) != 0:
            balances_not_null.append(f"[+] {balance['asset']} \n")

    if balances_not_null:
        return "Deine Kryptos aktuell:\n" + ", ".join(balances_not_null)

    return "Du hast aktuell keine Kryptowährungen.\n"


@app.route("/favourites", methods=['POST'])
def favourites(first_n_favorites: int = None):
    data = request.get_json()
    fav_stocks = data["stockList"]

    if first_n_favorites == 1:
        answer = "Dein 1. Favorit: \n"
    else:
        answer = "Deine Favoriten: \n"

    if first_n_favorites is None:
        first_n_favorites = len(fav_stocks)

    for ticker in fav_stocks[:min(len(fav_stocks), first_n_favorites)]:
        answer += ticker_info(ticker)

    return answer


@app.route("/leading", methods=['POST'])
def leading():
    data = request.get_json()
    stock_index = data["stockIndex"]
    answer = "Dein favorisierter Leitindex: \n"
    answer += ticker_info(stock_index)
    return answer


@app.route("/wallstreetbets", methods=['POST'])
def wallstreetbets():
    try:
        most_discussed = datasources.get_most_discussed_stock()
        name, value, currency = datasources.get_ticker_info(most_discussed["ticker"])

        return f"Auf r/wallstreetbets wird heute {name} mit {most_discussed['no_of_comments']} Kommentaren als {most_discussed['sentiment']} angesehen. " \
               f"Der aktuelle Wert liegt bei  {value} {currency}. \n"
    except Exception as e:
        print(e)
        return "Wallstreetbets kann gerade nicht abgerufen werden"


@app.route("/nft", methods=['POST'])
def nft():
    try:
        name, collection, hours_ago, value = datasources.get_top_nft()
        return f"{name} aus der Kollektion {collection} wurde vor {hours_ago} Stunden für {value} verkauft.\n"
    except Exception as e:
        print(e)
        return "NFT Informationen können gerade nicht abgerufen werden.\n"


@app.route("/info/<ticker>")
def ticker_info(ticker):
    try:
        name, value, currency = datasources.get_ticker_info(ticker)
        return f"{name} liegt aktuell bei {value:.2f} {currency}. \n"
    except Exception as e:
        print(e)
        return "Die Daten für dieses Kürzel konnten nicht abgerufen werden.\n"


