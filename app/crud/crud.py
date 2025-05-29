# project_root/app/crud/__init__.py
# (Empty file to make "crud" a Python package)

# project_root/app/crud/crud.py
# (Implement CRUD functions here)
from sqlalchemy.orm import Session
from app.models import models
from app.core.security import get_password_hash, verify_password
from app.schemas import schemas
from fastapi import HTTPException
from uuid import uuid4


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


def create_order(db: Session, user_id: int, order_data: schemas.CreateOrder):
    order = models.Order(
        order_number=str(uuid4()),
        user_id=user_id,
    )
    db.add(order)
    db.flush()
    for item in order_data.items:
        product = db.query(models.Product).filter(models.Product.number == item.product_number).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {item.product_number} not found")
        db.add(models.OrderDetail(order_id=order.id, product_id=product.id, quantity=item.quantity))
    db.commit()
    db.refresh(order)
    return order


def confirm_order(db: Session, order_id: int, shipping_address: str):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if order:
        order.shipping_address = shipping_address
        order.status = models.OrderStatus.confirmed
        db.commit()
        db.refresh(order)
        return order
    raise HTTPException(status_code=404, detail="Order not found")