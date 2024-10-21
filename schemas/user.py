from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    cedula: str
    name: str
    address: str
    phone: str
    email: str
    is_admin: Optional[bool]
    is_active: Optional[bool]

class UserCreate(UserBase):
    password: str
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
