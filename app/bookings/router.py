from fastapi import APIRouter

from app.bookings.schemas import BookingScheme
from app.bookings.service import BookingService


router = APIRouter(
    prefix="/bookings",
    tags=["Booking hotels"]
)


@router.get("")
async def get_bookings() -> list[BookingScheme]:
    return await BookingService.find_all()

