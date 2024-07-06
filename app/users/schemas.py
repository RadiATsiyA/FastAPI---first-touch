from pydantic import BaseModel, EmailStr


class UserAuthScheme(BaseModel):
    email: EmailStr
    password: str

