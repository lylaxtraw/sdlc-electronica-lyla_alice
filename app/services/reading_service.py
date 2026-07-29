# app/services/reading_service.py
from datetime import datetime
from app.repositories.reading_repo import ReadingRepository
from app.models.reading import ReadingModel

class ReadingService:
    def __init__(self, repo: ReadingRepository) -> None:
        self._repo = repo

    def record(self, sensor_id: str, value: float, unit: str) -> ReadingModel:
        if unit.upper() in ["C", "CELSIUS"] and value < -273.15:
            raise ValueError("Temperatura por debajo del cero absoluto")
        return self._repo.add(sensor_id, value, unit)

    def get_reading(self, reading_id: int) -> ReadingModel | None:
        return self._repo.get_by_id(reading_id)

    def list_readings(
        self, 
        sensor_id: str, 
        limit: int = 50, 
        offset: int = 0, 
        from_date: datetime | None = None, 
        to_date: datetime | None = None
    ) -> list[ReadingModel]:
        if from_date and to_date and from_date > to_date:
            raise ValueError("La fecha de inicio (from_date) no puede ser posterior a la fecha fin (to_date)")
        return self._repo.list_for_sensor(sensor_id, limit, offset, from_date, to_date)

    def update_reading(self, reading_id: int, value: float | None = None, unit: str | None = None) -> ReadingModel | None:
        if unit and unit.upper() in ["C", "CELSIUS"] and value is not None and value < -273.15:
            raise ValueError("Temperatura por debajo del cero absoluto")
        return self._repo.update(reading_id, value, unit)

    def delete_reading(self, reading_id: int) -> bool:
        return self._repo.delete(reading_id)