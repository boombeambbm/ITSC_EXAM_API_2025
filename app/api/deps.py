# project_root/app/api/__init__.py
# (Empty file to make "api" a Python package)

# project_root/app/api/deps.py
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from app.api.core.config import settings
from app.api.core.security import create_access_token
from app.api.db.session import SessionLocal
from app.api.models import models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Depends(settings.SECRET_KEY), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        user = db.query(models.User).get(int(user_id))
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token is invalid")
    