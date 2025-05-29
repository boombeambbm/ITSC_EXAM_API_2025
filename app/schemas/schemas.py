# project_root/app/schemas/__init__.py
# (Empty file to make "schemas" a Python package)

# project_root/app/schemas/schemas.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    phone: Optional[str] = None
    password: str
    confirm_password: str

class UserOut(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class OrderItem(BaseModel):
    product_number: str
    quantity: int

class CreateOrder(BaseModel):
    items: List[OrderItem]

class ConfirmOrder(BaseModel):
    shipping_address: str