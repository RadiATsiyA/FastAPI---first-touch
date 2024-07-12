from datetime import date

from sqlalchemy import select, func

from app.services.base import BaseServices
from app.database import async_session_maker
from app.hotels.models import Rooms
from app.bookings.models import Bookings


class RoomService(BaseServices):
    model = Rooms

    @classmethod
    async def find_all_available_rooms(cls, hotel_id: int, date_from: date, date_to: date):
        async with async_session_maker() as session:
            query = select(cls.model).where(cls.model.hotel_id == hotel_id)
            result = await session.execute(query)
            rooms = result.scalars().all()

            available_rooms = []
            for room in rooms:
                # Calculate the total price
                room.total_price = room.get_total_price(date_from, date_to)

                # Check availability and calculate rooms left
                bookings_query = select(func.count(Bookings.id)).filter(
                    Bookings.room_id == room.id,
                    Bookings.date_from < date_to,
                    Bookings.date_to > date_from
                )
                bookings_result = await session.execute(bookings_query)
                rooms_booked = bookings_result.scalar()

                room.rooms_left = max(room.quantity - rooms_booked, 0)

                available_rooms.append(room)

                return available_rooms

