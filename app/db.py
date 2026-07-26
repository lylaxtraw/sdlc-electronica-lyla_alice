# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# 1. El Engine: Es el driver de bajo nivel que habla con la base de datos (nuestro "periférico")
# connect_args={"check_same_thread": False} es necesario para SQLite en FastAPI (que es asíncrono/multihilo)
engine = create_engine("sqlite:///sensorhub.db", connect_args={"check_same_thread": False})

# 2. SessionLocal: Es la fábrica de sesiones. Una sesión es como una "transacción en memoria"
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

# 3. Base: La clase madre de la que heredarán todos nuestros modelos ORM
class Base(DeclarativeBase):
    pass