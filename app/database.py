from typing import List, Optional
from models import Event
from datetime import datetime
from utils import make_naive

# Simulating in-memory database with a list
events_db = []


def add_event(event: Event):
    events_db.append(event)
    return event


def get_event_by_id(event_id: int) -> Optional[Event]:
    for event in events_db:
        if event.id == event_id:
            return event
    return None


def get_events_in_range(from_time: datetime, to_time: datetime) -> List[Event]:
    return [event for event in events_db if from_time <= make_naive(event.time) <= to_time]
