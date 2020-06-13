# author        : Esteban
# name          : utils.py
# date          : 2020
# python_version: 3.7
# notes         : StocksAdventures
# ==============================================================================
import os
import os.path
from pathlib import Path


def createDir(dir_path):
    is_dir = os.path.isdir(dir_path)
    if not is_dir:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
