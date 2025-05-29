# project_root/app/models/__init__.py
# (Empty file to make "models" a Python package)

# project_root/app/models/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from app.db.base import Base
from enum import Enum as PyEnum

class OrderStatus(PyEnum):
    pending = "รอยืนยันคำสั่งซื้อ"
    confirmed = "ยืนยันคำสั่งซื้อ"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String, nullable=True)
    hashed_password = Column(String)
    orders = relationship("Order", back_populates="user")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    number = Column(String, unique=True)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    shipping_address = Column(Text, nullable=True)
    status = Column(Enum(OrderStatus), default=OrderStatus.pending)
    user = relationship("User", back_populates="orders")
    details = relationship("OrderDetail", back_populates="order")

class OrderDetail(Base):
    __tablename__ = "order_details"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    order = relationship("Order", back_populates="details")