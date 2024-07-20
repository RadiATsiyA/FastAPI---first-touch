from pydantic import BaseModel
from datetime import date


class BookingScheme(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int = None
    total_days: int = None

    class Config:
        from_attributes = True
