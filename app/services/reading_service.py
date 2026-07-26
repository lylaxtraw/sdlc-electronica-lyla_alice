# app/services/reading_service.py
from app.repositories.reading_repo import ReadingRepository
from app.models.reading import ReadingModel

class ReadingService:
    """Lógica de negocio. Depende de la abstracción del repositorio (DIP)."""
    
    # Inyección de Dependencias
    def __init__(self, repo: ReadingRepository) -> None:
        self._repo = repo
 
    def record(self, sensor_id: str, value: float, unit: str) -> ReadingModel:
        # Validación de física real
        if unit.upper() in ["C", "CELSIUS"] and value < -273.15:
            raise ValueError("Temperatura por debajo del cero absoluto")
            
        return self._repo.add(sensor_id, value, unit)