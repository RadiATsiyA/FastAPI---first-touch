from typing import List

from pydantic import BaseModel


class RoomsScheme(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    price: int
    services: List[str]
    quantity: int
    image_id: int
