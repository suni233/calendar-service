from pydantic import BaseModel
from datetime import datetime


class Event(BaseModel):
    id: int
    description: str
    time: datetime
