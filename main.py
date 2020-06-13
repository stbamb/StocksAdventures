# author        : Esteban
# name          : main.py
# date          : 2020
# usage         : python3 main.py
# python_version: 3.7
# notes         : StocksAdventures
# ==============================================================================
import config
import stock_data_retriever


def main():
    tickers = config.TICKERS_WATCHLIST
    stock_data_retriever.downloadHistoricalData(tickers)


if __name__ == "__main__":
    main()
