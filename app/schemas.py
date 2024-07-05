from pydantic import BaseModel
from typing import Optional
from datetime import date

from fastapi import Query


class HotelSchema(BaseModel):
    name: str
    location: str
    date_from: date
    date_to: date
    stars: Optional[int] = Query(None, ge=1, le=5)


class BookingSchema(BaseModel):
    hotel_id: int
    date_from: date
    date_to: date
