# author        : Esteban
# name          : stock_data_retriever.py
# date          : 2020
# python_version: 3.7
# notes         : StocksAdventures
# ==============================================================================
from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf

import config
import utils


def downloadHistoricalData(ticker_list):
    utils.createDir(config.STOCKS_DATA_FOLDER)
    if _outdatedData():
        _retrieveStockHistorical(ticker_list)
        _retrieveStockDetailedHistorical(ticker_list)


def _outdatedData():
    if utils.isBizDay(datetime.today().date()):
        return False
    return utils.areHistoricalsOutdated(config.STOCKS_DATA_FOLDER)


def _retrieveStockHistorical(ticker_list):
    starting_date = datetime.strptime(config.STOCK_INITIAL_DATE, config.DATE_FORMAT).date()
    for ticker in ticker_list:
        stock_info = pd.DataFrame(yf.download(ticker, start=starting_date)).round(config.DECIMALS_PRECISION)
        stock_info.to_csv(config.STOCKS_DATA_FOLDER + ticker + config.DAILY_STOCK_HISTORICAL_FILE_EXTENSION)
    if config.DEBUG:
        print("Downloaded historical data for all tickers")


def _retrieveStockDetailedHistorical(ticker_list):
    for ticker in ticker_list:
        final_date = datetime.today().date()
        starting_date = final_date - timedelta(days=29)
        iteration = 0
        flag = True
        mode = 'w'
        while starting_date < final_date:
            stock_info = pd.DataFrame(yf.download(ticker, start=starting_date, end=starting_date + timedelta(days=7),
                                                  interval=config.DETAILED_STOCK_PRICE_INTERVAL)).round(
                config.DECIMALS_PRECISION)
            stock_info.to_csv(config.STOCKS_DATA_FOLDER + ticker + config.DETAILED_STOCK_HISTORICAL_FILE_EXTENSION,
                              mode=mode, header=flag)
            starting_date += timedelta(days=7)
            iteration += 1
            if iteration > 0:
                mode = 'a'
                flag = False
    if config.DEBUG:
        print("Downloaded detailed historical data for all tickers")
