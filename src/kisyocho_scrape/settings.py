import json
from pathlib import Path
from typing import Any, Dict, List, Union
import yaml

import schemas


place46_no_jf = Path(__file__).parent / 'place46_no.json'
with open(place46_no_jf, 'r') as f:
    place46_no: Dict[str, schemas.PlaceNo] = json.load(f)

columns: List[str] = ['時', '気圧', '海面気圧','降水量','気温','露点温度','蒸気圧','湿度','風速','風向','日照時間','全天日射量','降雪','積雪','天気','雲量','視程']
