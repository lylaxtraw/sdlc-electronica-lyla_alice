# app/models/reading.py
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
from app.db import Base

class ReadingModel(Base):
    __tablename__ = "readings"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    # Conectamos el sensor_id directamente a sensors.id
    sensor_id: Mapped[str] = mapped_column(ForeignKey("sensors.id"), index=True)
    
    value: Mapped[float]
    unit: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))

    # Relación inversa: Cada lectura pertenece a un sensor
    sensor: Mapped["SensorModel"] = relationship(back_populates="readings")