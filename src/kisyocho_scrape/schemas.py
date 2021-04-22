from typing import Any, List, Dict, Union, NewType
from dataclasses import dataclass


@dataclass
class PlaceNo:
    place: str
    prec_no: int
    block_no: int
