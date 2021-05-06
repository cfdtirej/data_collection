from pathlib import Path
from typing import Any, List, Dict, Iterator

import numpy as np
import pandas as pd
from influxdb import InfluxDBClient


def csv_to_lineprotocol(
    csvfile: Path, database: str, measurement: str, tags: Dict[str, str] = None
) -> Iterator[Dict[str, Any]]:
    if not tags:
        tags = {'measurement': measurement}
    df = pd.read_csv(csvfile, index_col=0)
    df.index = pd.to_datetime(df.index).tz_localize('Asia/Tokyo')
    for ts, vals in zip(df.index, df.values):
        fields = {}
        for col, val in zip(df.columns, vals):
            if type(val) == (float or int):
                if not np.isnan(val):
                    fields[col] = val
            else:
                fields[col] = val
        lineprotocol: List[Dict[str, Any]] = [{
            'time': ts.isoformat(),
            'measurement': measurement,
            'tags': tags,
            'fields': fields
        }]
        yield lineprotocol

if __name__ == '__main__':
    csvfiles = Path(__file__).parents[1] / 'kisyocho_scrape' / 'past_weather'
    csvfiles = csvfiles.glob('**/*.csv')
    for csvfile in csvfiles:
        for lineprotocol in csv_to_lineprotocol(csvfile=csvfile,measurement='hello', database='db'):
            print(lineprotocol)
