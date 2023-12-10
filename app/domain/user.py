from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
