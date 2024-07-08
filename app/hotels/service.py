from pydantic import Json
from sqlalchemy import insert

from app.database import async_session_maker
from app.services.base import BaseServices
from app.hotels.models import Hotels


class HotelsService(BaseServices):
    model = Hotels

    @classmethod
    async def add(cls, name: str, location: str, services: Json,
                  rooms_quantity: int, image_id: int):
        async with async_session_maker() as session:
            add_hotel = insert(cls.model).values(
                name=name, location=location,
                services=services,
                rooms_quantity=rooms_quantity,
                image_id=image_id
            ).returning(cls.model)
            new_hotel = await session.execute(add_hotel)
            await session.commit()
            return new_hotel.scalar_one_or_none()



