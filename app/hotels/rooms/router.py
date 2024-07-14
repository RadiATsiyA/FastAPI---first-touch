from datetime import date

from fastapi_cache.decorator import cache

from app.exeptions import InvalidDateRangeException
from app.hotels.router import router
from app.hotels.rooms.service import RoomService


@router.get("/{hotel_id}/rooms")
@cache(expire=60)
async def get_rooms(hotel_id: int, date_from: date, date_to: date):
    if date_from > date_to:
        raise InvalidDateRangeException
    return await RoomService.find_all_available_rooms(hotel_id=hotel_id, date_from=date_from, date_to=date_to)


