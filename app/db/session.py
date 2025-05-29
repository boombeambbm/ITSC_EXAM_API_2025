# project_root/app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# เชื่อมต่อกับ MySQL ผ่าน localhost/phpmyadmin
DATABASE_URL = os.getenv("http://localhost/phpmyadmin/index.php?route=/database/structure&db=api_exam", "mysql+pymysql://root:password@127.0.0.1/api_exam")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
