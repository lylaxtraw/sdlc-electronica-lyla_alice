# tests/test_services.py
from datetime import UTC, datetime

import pytest
from fastapi import HTTPException

from app.models.reading import ReadingModel
from app.models.sensor import SensorModel
from app.services.reading_service import ReadingService


# 1. El Simulador de Base de Datos en RAM
class FakeReadingRepository:
    def __init__(self) -> None:
        self.readings: list[ReadingModel] = []
        self._id_counter = 1

    def add(self, sensor_id: int, value: float, unit: str) -> ReadingModel:
        reading = ReadingModel(
            id=self._id_counter,
            sensor_id=sensor_id,
            value=value,
            unit=unit,
            created_at=datetime.now(UTC)
        )
        self.readings.append(reading)
        self._id_counter += 1
        return reading

    def list_for_sensor(self, sensor_id: int) -> list[ReadingModel]:
        return [r for r in self.readings if r.sensor_id == sensor_id]

class FakeSensorRepository:
    def get_by_id(self, sensor_id: int):
        return SensorModel(
            id=sensor_id,
            name="Sensor de Prueba",
            type="T",
            unit="C",
            min_value=-273.15,
            max_value=100.0
        )

# 2. Las Pruebas Unitarias (¡A la velocidad de la luz!)
def test_record_reading_success():
    # Arrange (Preparar)
    fake_reading = FakeReadingRepository()
    fake_sensor = FakeSensorRepository()
    
    # Act (Actuar)
    service = ReadingService(fake_reading, fake_sensor)
    nueva_lectura = service.record_reading(sensor_id=1, value=25.0, unit="C")
    
    # Assert (Afirmar)
    assert nueva_lectura.id == 1
    assert nueva_lectura.value == 25.0
    assert len(fake_reading.readings) == 1

def test_record_reading_below_absolute_zero_raises_error():
    # Arrange
    fake_reading = FakeReadingRepository()
    fake_sensor = FakeSensorRepository()

    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        service = ReadingService(fake_reading, fake_sensor)
        service.record_reading(1, -274.0, "C")

    # Verificamos que el código de error sea 422 y tenga el texto correcto
    assert exc_info.value.status_code == 422
    assert "fuera de rango físico" in exc_info.value.detail
    
    # Verificamos que la BD fake sigue intacta
    assert len(fake_reading.readings) == 0