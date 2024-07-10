from datetime import date

from fastapi import APIRouter, Depends

from app.bookings.schemas import BookingScheme
from app.bookings.service import BookingService
from app.exeptions import RoomCannotBeBookedException
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[BookingScheme]:
    return await BookingService.find_all(user_id=user.id)


@router.post("")
async def add_booking(room_id: int, date_form: date, date_to: date,
                      user: Users = Depends(get_current_user)):
    booking = await BookingService.add(user.id, room_id, date_form, date_to)
    if not booking:
        raise RoomCannotBeBookedException


@router.delete("/{id}/")
async def delete_booking(id: int, user: Users = Depends(get_current_user)):
    return await BookingService.delete(model_id=id)

