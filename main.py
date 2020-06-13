# author        : Esteban
# name          : main.py
# date          : 2020
# usage         : python3 main.py
# python_version: 3.7
# notes         : StocksAdventures
# ==============================================================================

from datetime import date, timedelta

import pandas as pd
import yfinance as yf

import config
import stock_prediction_tools
import utils


def main():
    utils.createDir(config.STOCKS_DATA_FOLDER)
    tickers = stock_prediction_tools.getTickers()

    today = date.today()
    this_week = today - timedelta(days=5)
    year_start = str(date.today().year) + config.STOCK_INITIAL_DATE
    today = today.strftime(config.DATE_FORMAT)

    print(year_start)
    print(today)

    izea = pd.DataFrame(yf.download(tickers, start=this_week, end=today, interval=config.STOCK_PRICE_INTERVAL))

    # izea.to_csv(config.STOCKS_DATA_FOLDER + 'idex.csv')

    df = pd.DataFrame(izea)
    print(izea)
    #
    # for index, row in df.iterrows():
    #     print(row['Open'])

    crazy_days = determineCrazyDays(izea)
    print(crazy_days.shape)
    print(crazy_days.to_string())


def determineCrazyDays(stocks_info):
    dates = []
    for index, row in stocks_info.iterrows():
        open = float(row['Open'])
        high = float(row['High'])
        if open + open * config.RISE_PERCENTAGE < high:
            dates.append(row)
    return pd.DataFrame(dates)


if __name__ == "__main__":
    main()
