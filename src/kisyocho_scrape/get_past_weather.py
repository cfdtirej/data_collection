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
    if not area in settings.place46_no.keys():
        raise f'{area}以外の地域を選択してください'
    area_numbers: schemas.PlaceNo = settings.place46_no[area]
    prec_no: int =  area_numbers['prec_no']
    block_no: int = area_numbers['block_no']
    
    # request to kishocho
    url: str = f'https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?prec_no={prec_no}&block_no=47605&year={year_}&month={month_}&day={day_}&view='
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')

    data_table: List[List[str]] = [settings.wheater_tb_columns]
    for tr in soup.findAll('tr', class_='mtx'):
        td = tr.findAll('td')
        row: List[str] = [t.string for t in td]
        img = tr.findAll('img')
        icon: str = img[0]['src'] if len(img) else ''
        alt: str = img[0]['alt'] if len(img) else ''
        data = []
        for idx, val in enumerate(row):
            if idx == 14:
                data.append(alt)
            else:
                data.append(val)
        if len(data) > 0:
            data.insert(15, icon)
            data_table.append(data)
        
    return data_table


if __name__ == '__main__':
    get_past_weather_table('金沢',2020,1,2)