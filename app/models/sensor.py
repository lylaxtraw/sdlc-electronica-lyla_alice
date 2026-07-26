# app/models/sensor.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base

class SensorModel(Base):
    __tablename__ = "sensors"

    # ID será algo como "TEMP-01" 
    id: Mapped[str] = mapped_column(primary_key=True)
    
    # Tipo de sensor: "temperature", "humidity"
    sensor_type: Mapped[str] 
    
    # Umbrales físicos para validar las lecturas (pueden ser nulos si no aplican)
    min_threshold: Mapped[float | None]
    max_threshold: Mapped[float | None]

    # Relación 1-a-N: Un sensor tiene muchas lecturas
    # (El string "ReadingModel" le dice que busque esa clase)
    readings: Mapped[list["ReadingModel"]] = relationship(back_populates="sensor", cascade="all, delete-orphan")