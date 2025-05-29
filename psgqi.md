app/
├── api/
│   ├── __init__.py
│   ├── admin.py        # Admin routes with Basic Auth
│   ├── auth.py         # Login route (JWT)
│   ├── deps.py         # Dependencies (get_db, get_current_user)
│   └── user.py         # Register route
├── core/
│   ├── config.py       # App settings from .env
│   └── security.py     # Password hashing + JWT functions
├── crud/
│   ├── __init__.py
│   └── crud.py         # Logic for DB access
├── db/
│   ├── __init__.py
│   ├── base.py         # Declarative base
│   └── session.py      # SQLAlchemy session/engine
├── models/
│   ├── __init__.py
│   └── models.py       # SQLAlchemy models
├── schemas/
│   ├── __init__.py
│   └── schemas.py      # Pydantic schemas
└── main.py             # FastAPI entry point
