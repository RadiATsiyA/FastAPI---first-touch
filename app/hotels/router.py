from fastapi import APIRouter, Depends
from pydantic import Json

from app.exeptions import HotelAddingErrorException, UserIsNotAuthorized
from app.hotels.schemas import HotelsScheme
from app.hotels.service import HotelsService
from app.users.models import Users
from app.users.dependencies import get_current_user


router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("")
async def get_hotels(
        name: str | None = None, location: str | None = None, services: str | None = None,
        rooms_quantity: int | None = None, image_id: int | None = None):
    return await HotelsService.find_all()


@router.post("")
async def add_hotel(
        name: str, location: str, services: str,
        rooms_quantity: int, image_id: int,
        user: Users = Depends(get_current_user)):

    if not user:
        raise UserIsNotAuthorized
    new_hotel = await HotelsService.add(name=name, location=location,
                                        services=services, rooms_quantity=rooms_quantity,
                                        image_id=image_id)
    if not new_hotel:
        raise HotelAddingErrorException
    return new_hotel
