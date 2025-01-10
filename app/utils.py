from datetime import datetime
from typing import Optional


def parse_datetime(datetime_str: str, format: Optional[str] = "%Y-%m-%dT%H:%M:%S") -> datetime:
    try:
        return datetime.strptime(datetime_str, format)
    except ValueError:
        return None


def make_naive(dt: datetime) -> datetime:
    return dt.replace(tzinfo=None)
