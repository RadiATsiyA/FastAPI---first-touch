from fastapi import APIRouter, Depends

from app.bookings.schemas import BookingScheme
from app.bookings.service import BookingService
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Booking hotels"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[BookingScheme]:
    return await BookingService.find_all(user_id=user.id)

