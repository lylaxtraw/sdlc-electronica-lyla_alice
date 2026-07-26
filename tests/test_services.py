# tests/test_services.py
import pytest
from datetime import datetime, timezone
from app.services.reading_service import ReadingService
from app.models.reading import ReadingModel

# 1. El Simulador de Base de Datos en RAM
class FakeReadingRepository:
    def __init__(self):
        self.readings: list[ReadingModel] = []
        self._id_counter = 1

    def add(self, sensor_id: str, value: float, unit: str) -> ReadingModel:
        reading = ReadingModel(
            id=self._id_counter,
            sensor_id=sensor_id,
            value=value,
            unit=unit,
            created_at=datetime.now(timezone.utc)
        )
        self.readings.append(reading)
        self._id_counter += 1
        return reading

    def list_for_sensor(self, sensor_id: str) -> list[ReadingModel]:
        return [r for r in self.readings if r.sensor_id == sensor_id]

# 2. Las Pruebas Unitarias (¡A la velocidad de la luz!)
def test_record_reading_success():
    # Arrange (Preparar)
    repo = FakeReadingRepository()
    service = ReadingService(repo)
    
    # Act (Actuar)
    reading = service.record("TEMP-01", 25.0, "C")
    
    # Assert (Afirmar)
    assert reading.id == 1
    assert reading.value == 25.0
    assert len(repo.readings) == 1

def test_record_reading_below_absolute_zero_raises_error():
    # Arrange
    repo = FakeReadingRepository()
    service = ReadingService(repo)
    
    # Act & Assert
    with pytest.raises(ValueError, match="Temperatura por debajo del cero absoluto"):
        service.record("TEMP-01", -274.0, "C")
        
    # Verificamos que la BD fake sigue intacta, porque lanzó error antes de guardar
    assert len(repo.readings) == 0