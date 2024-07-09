from pydantic import Json
from sqlalchemy import insert, select

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

    @classmethod
    async def find_all(cls, filters: dict):
        async with async_session_maker() as session:
            query = select(cls.model)
            for key, value in filters.items():
                if value is not None:
                    if isinstance(value, str):
                        query = query.filter(getattr(cls.model, key).ilike(f"%{value}%"))
                    else:
                        query = query.filter(getattr(cls.model, key) == value)
            result = await session.execute(query)
            return result.scalars().all()





