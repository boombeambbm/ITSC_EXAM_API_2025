# project_root/app/api/auth.py
from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from app.core.security import create_access_token
from app.crud import crud
from app.api.deps import get_db

router = APIRouter()

@router.post("/login")
def login(email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}