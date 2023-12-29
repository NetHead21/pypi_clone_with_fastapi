import datetime
from dataclasses import dataclass


@dataclass
class Release:
    version: str
    created_date: datetime.datetime
