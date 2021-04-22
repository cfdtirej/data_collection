import csv
import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict

import pytz
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

import settings
import schemas


_year = '2002'
_month = '2'
_day = '1'
past_url = f'https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?prec_no=56&block_no=47605&year={_year}&month={_month}&day={_day}&view='

res = requests.get(past_url)
res.encoding = res.apparent_encoding

soup = BeautifulSoup(res.text, 'html.parser')
table_text = soup.find('table').get_text()
print(table_text)


if __name__ == '__main__':
    pass