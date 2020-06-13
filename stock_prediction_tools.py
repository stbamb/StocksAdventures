# author        : Esteban
# name          : stock_prediction_tools.py
# date          : 2020
# python_version: 3.7
# notes         : StocksAdventures
# ==============================================================================
import pandas as pd

import config


def determineCrazyDays(stocks_info):
    dates = []
    for index, row in stocks_info.iterrows():
        open = float(row['Open'])
        high = float(row['High'])
        if open + open * config.RISE_PERCENTAGE < high:
            dates.append(row)
    return pd.DataFrame(dates)
