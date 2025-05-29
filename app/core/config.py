# project_root/app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ADMIN_USER: str
    ADMIN_PASSWORD: str
    RUN_MODE: str = "dev"

    class Config:
        env_file = ".env"

settings = Settings()