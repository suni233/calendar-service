import os
import uvicorn
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from datetime import datetime
from models import Event
from utils import parse_datetime
from database import add_event, get_event_by_id, get_events_in_range

app = FastAPI(title="Calendar Service API")


@app.get("/")
async def index():
    return {
        "message": "Welcome to Calender Service"
    }


@app.post("/events", response_model=Event)
async def create_event(event: Event):
    return add_event(event)


@app.get("/events/{event_id}", response_model=Event)
async def get_event(event_id: int, datetime_format: Optional[str] = "%Y-%m-%dT%H:%M:%S"):
    event = get_event_by_id(event_id)
    if event is None:
        raise HTTPException(status_code=404, detail=f"Event not found with ID {event_id}")
    return event


@app.get("/events", response_model=List[Event])
async def get_events(datetime_format: Optional[str] = "%Y-%m-%dT%H:%M:%S",
                     from_time: Optional[str] = None,
                     to_time: Optional[str] = None):
    now = datetime.now()
    start_of_day = datetime(now.year, now.month, now.day)

    from_time = parse_datetime(from_time, datetime_format) if from_time else start_of_day
    to_time = parse_datetime(to_time, datetime_format) if to_time else now

    events = get_events_in_range(from_time, to_time)
    return events


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host=host, port=port)
