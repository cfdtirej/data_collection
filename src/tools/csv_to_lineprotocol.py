from pathlib import Path
from typing import Any, List, Dict, Iterator

import numpy as np
import pandas as pd
from influxdb import InfluxDBClient


def csv_to_lineprotocol(
    csvfile: Path, database: str, measurement: str, tags: Dict[str, str]
) -> Iterator[Dict[str: Any]]:
    df = pd.read_csv(csvfile, col=0)
    df.index = pd.to_datetime(df.index).tz_localize('Asia/Tokyo')
    for ts, vals in zip(df.index, df.values):
        fields = {}
        for col, val in zip(df.columns, vals):
            if not np.isnan(val):
                fields[col] = val
        lineprotocol: List[Dict[str, Any]] = [{
            'time': ts.isoformat(),
            'measurement': measurement,
            'tags': tags,
            'fields': fields
        }]
        yield lineprotocol
