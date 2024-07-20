from datetime import date

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from pydantic import parse_obj_as
from sqlalchemy.orm import selectinload

from app.bookings.models import Bookings
from app.bookings.schemas import BookingScheme
from app.bookings.service import BookingService
from app.database import async_session_maker
from app.exeptions import RoomCannotBeBookedException
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.get("")
@cache(expire=60)
async def get_bookings(user: Users = Depends(get_current_user)) -> list[BookingScheme]:
    return await BookingService.find_all(user_id=user.id)


@router.post("")
async def add_booking(room_id: int, date_form: date, date_to: date,
                      user: Users = Depends(get_current_user)):
    booking = await BookingService.add(user.id, room_id, date_form, date_to)
    if not booking:
        raise RoomCannotBeBookedException

    async with async_session_maker() as session:
        booking = await session.get(Bookings, booking.id, options=[selectinload('*')])

    booking_dict = parse_obj_as(BookingScheme, booking).dict()
    send_booking_confirmation_email.delay(booking_dict, user.email)
    return booking_dict


@router.delete("/{id}/")
async def delete_booking(id: int, user: Users = Depends(get_current_user)):
    return await BookingService.delete(model_id=id)

