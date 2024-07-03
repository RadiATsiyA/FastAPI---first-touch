from pydantic import BaseModel
from datetime import date

from typing import List


class Genre(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    writer: str
    duration: str = None
    date: date = None
    summary: str = None
    genres: List[Genre]
