from fastapi import APIRouter, HTTPException
from app.users.schemas import UserRegisterScheme
from app.users.service import UserService
from app.users.auth import get_password_hash

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Users"]
)


@router.post("/register")
async def register_user(user_data: UserRegisterScheme):
    existing_user = await UserService.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=400)
    hashed_password = get_password_hash(user_data.password)
    await UserService.add(email=user_data.email, password=hashed_password)


