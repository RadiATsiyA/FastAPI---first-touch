from typing import List, Optional

from fastapi import APIRouter, Depends, Query

from app.exeptions import HotelAddingErrorException, UserIsNotAuthorized, HotelUpdateErrorExecption
from app.hotels.schemas import HotelCreateUpdateScheme, HotelsGetScheme
from app.hotels.service import HotelsService
from app.users.models import Users
from app.users.dependencies import get_current_user


router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("", response_model=List[HotelsGetScheme])
async def get_hotels(
        name: Optional[str] = Query(None),
        location: Optional[str] = Query(None),
        rooms_quantity: Optional[int] = Query(None)
):
    filters = {
        'name': name,
        'location': location,
        'rooms_quantity': rooms_quantity
    }

    return await HotelsService.find_all(filters)


@router.post("")
async def add_hotel(
        hotel: HotelCreateUpdateScheme,
        user: Users = Depends(get_current_user)
):
    if not user:
        raise UserIsNotAuthorized
    new_hotel = await HotelsService.add(name=hotel.name, location=hotel.location,
                                        services=hotel.services, rooms_quantity=hotel.rooms_quantity,
                                        image_id=hotel.image_id)
    if not new_hotel:
        raise HotelAddingErrorException
    return new_hotel


@router.put("/{id}/")
async def update_hotel(
        hotel: HotelCreateUpdateScheme,
        user: Users = Depends(get_current_user)
):
    data = hotel.dict(exclude_unset=True)
    try:
        return await HotelsService.update(model_id=hotel.id, name=hotel.name, location=hotel.location,
                                          services=hotel.services, rooms_quantity=hotel.rooms_quantity,
                                          image_id=hotel.image_id)
    except Exception:
        raise HotelUpdateErrorExecption


@router.delete("/{id}/")
async def delete_hotel(id: int, user: Users = Depends(get_current_user)):
    return await HotelsService.delete(model_id=id)
