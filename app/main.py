from fastapi import FastAPI
from schemas import HotelSchema, BookingSchema


app = FastAPI()


@app.get("hotels")
def get_hotels_list(hotels: int, location: str, stars: str = None):
    return hotels


@app.post("/booking")
def book_hotel(booking_hotel: BookingSchema):
    return booking_hotel

