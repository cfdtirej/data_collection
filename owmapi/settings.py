import csv
import json
import requests
from typing import List, Dict, TypedDict, Union
from dataclasses import dataclass
from pathlib import Path

import pytz
import yaml


Api = TypedDict('Api', {'Key': str})

@dataclass
class Settings:
    API: Api


settings_yaml = Path(__file__).parent / 'settings.yaml'
with open(settings_yaml, 'r') as f:
    settings: Settings = yaml.safe_load(f)
city = {
    'id': 1849584, 
    'name': 'Tsurugi-asahimachi', 
    'coord': {'lat': 36.45, 'lon': 136.6333}, 
    'country': 'JP', 
    'population': 0, 
    'timezone': 32400, 
    'sunrise': 1616705321, 
    'sunset': 1616749775
}
# url = f'http://api.openweathermap.org/data/2.5/forecast?id=1849584&appid={}'
url = f'http://api.openweathermap.org/data/2.5/weather?id={city["id"]}&appid={settings["API"]["Key"]}'
one_call_api = f'https://api.openweathermap.org/data/2.5/onecall?lat={city["coord"]["lat"]}&lon={city["coord"]["lon"]}&exclude=minutely&appid={settings["API"]["Key"]}&lang=ja'
# get = requests.get(url)
# print(get.json())
from pprint import pprint
res = requests.get(one_call_api)
pprint(res.json())