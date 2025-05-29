# project_root/app/api/order.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.api.deps import get_db, get_current_user
from app.crud import crud

router = APIRouter()

@router.post("/")
def create_order(order: schemas.CreateOrder, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud.create_order(db, user_id=current_user.id, order_data=order)

@router.post("/{order_id}/confirm")
def confirm_order(order_id: int, data: schemas.ConfirmOrder, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud.confirm_order(db, order_id=order_id, shipping_address=data.shipping_address)