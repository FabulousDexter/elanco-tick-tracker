from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class TickData(SQLModel, table=True):
    id: str = Field(primary_key=True)
    timestamp: datetime
    location: str
    species: str
    latin_name: str
