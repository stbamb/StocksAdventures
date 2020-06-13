# author        : Esteban
# name          : utils.py
# date          : 2020
# python_version: 3.7
# notes         : StocksAdventures
# ==============================================================================
import os
import os.path, time
from datetime import datetime
from pathlib import Path

import pandas as pd


def createDir(dir_path):
    is_dir = os.path.isdir(dir_path)
    if not is_dir:
        Path(dir_path).mkdir(parents=True, exist_ok=True)


def isBizDay(today):
    return bool(len(pd.bdate_range(today, today)))


def areHistoricalsOutdated(directory):
    last_modified = 0
    for filename in os.listdir(directory):
        last_modified = time.ctime(os.path.getmtime(directory + filename))
        break
    # last_modified = datetime.date(last_modified)
    print(last_modified)
    if last_modified == 0:
        return True

