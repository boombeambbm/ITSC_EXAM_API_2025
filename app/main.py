# project_root/app/__init__.py
# (Empty file to make "app" a Python package)

# project_root/app/main.py
from fastapi import FastAPI
from app.api import user, auth, order, admin
from app.db.session import engine
from app.models import models
from app.core.config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce Order Management API")
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(order.router, prefix="/orders", tags=["Orders"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
