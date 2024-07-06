from pydantic import BaseModel, EmailStr


class UserRegisterScheme(BaseModel):
    email: EmailStr
    password: str

