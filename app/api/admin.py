# project_root/app/api/admin.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.core.config import settings
from app.models import models

router = APIRouter()
security = HTTPBasic()


def verify_admin(credentials: HTTPBasicCredentials = Depends(security)):
    correct = credentials.username == settings.ADMIN_USER and credentials.password == settings.ADMIN_PASSWORD
    if not correct:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid admin credentials")

@router.get("/orders", dependencies=[Depends(verify_admin)])
def list_all_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()