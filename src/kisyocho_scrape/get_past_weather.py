import csv
import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Union

import pytz
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

import settings
import schemas


def get_past_weather_table(area: str, year_: str, month_: str, day_: str) -> List[str]:
    data_table = [settings.wheater_tb_columns]
    if not area in settings.place46_no.keys():
        raise f'{area}以外の地域を選択してください'
    area_numbers: schemas.PlaceNo = settings.place46_no[area]
    prec_no, block_no = area_numbers['prec_no'], area_numbers['block_no']
    url = f'https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?prec_no={prec_no}&block_no=47605&year={year_}&month={month_}&day={day_}&view='
    
    # request to kishocho
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text)
    for tr in soup.findAll('tr', class_='mtx'):
        td = tr.findAll('td')
        row = [t.string for t in td]
        if len(row):
            data_table.append(row)
    return data_table

_year = '2002'
_month = '2'
_day = '1'
past_url = f'https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?prec_no=56&block_no=47605&year={_year}&month={_month}&day={_day}&view='

res = requests.get(past_url)
res.encoding = res.apparent_encoding

soup = BeautifulSoup(res.text)
table_rows = soup.findAll('tr',class_='mtx')
print(table_rows)
data_table = [settings.wheater_tb_columns]
for tr in table_rows:
    td = tr.findAll('td')
    img = [[i['src'], i['alt']] for i in tr.findAll('img')]
    
    # print(td)
    print(img,alt)
    if data:
        data_table.append(data)


# print(data_table)
if __name__ == '__main__':
    pass