from typing import List

from pydantic import BaseModel


class HotelCreateUpdateScheme(BaseModel):
    name: str
    location: str
    services: List[str]
    rooms_quantity: int
    image_id: int

    class Config:
        from_attributes = True


class HotelsGetScheme(BaseModel):
    id: int
    name: str
    location: str
    services: List[str]
    rooms_quantity: int
    image_id: int
