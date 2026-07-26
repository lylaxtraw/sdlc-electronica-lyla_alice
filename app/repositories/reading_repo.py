# app/repositories/reading_repo.py
from typing import Protocol
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.reading import ReadingModel

# 1. El Contrato (DIP)
class ReadingRepository(Protocol):
    def add(self, sensor_id: str, value: float, unit: str) -> ReadingModel: ...
    def list_for_sensor(self, sensor_id: str) -> list[ReadingModel]: ...

# 2. La Implementación Real (Producción)
class SQLAlchemyReadingRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, sensor_id: str, value: float, unit: str) -> ReadingModel:
        reading = ReadingModel(sensor_id=sensor_id, value=value, unit=unit)
        self.session.add(reading)
        self.session.commit()
        self.session.refresh(reading)  # Recarga el objeto para obtener su ID generado
        return reading

    def list_for_sensor(self, sensor_id: str) -> list[ReadingModel]:
        # Sintaxis moderna de SQLAlchemy 2.0
        stmt = select(ReadingModel).where(ReadingModel.sensor_id == sensor_id)
        return list(self.session.scalars(stmt).all())