import csv
import requests
from datetime import datetime, timedelta
from pathlib import Path

import datetime_string_range

for ts in datetime_string_range.daterange_strings():
    dtstr = ts.isoformat().replace('-', '')

    url = f'http://www.rikuden.co.jp/nw/denki-yoho/csv/juyo_05_{dtstr}.csv'
    res = requests.get(url)
    data = [[t for t in txt.split(',')] for txt in res.text.splitlines()]
    
    csv_dir = Path(__file__).parent / 'demand_csv' / f'{ts.year}' / f'{ts.month}'
    if not csv_dir.is_dir():
        csv_dir.mkdir(parents=True)
    csv_file = csv_dir / f'{dtstr}.csv'
    if not csv_dir.exists():
        csv_file.touch()
    with open(csv_file, 'w') as f:
        wirter = csv.writer(f)
        wirter.writerows(data)


# data = [i for i in res.text.splitlines()]
# print(data)
# print(res.text.splitlines())
# data_list = [string for string in res.text.splitlines()]
# print(data_list)
# with open('./data.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows(data_list)
