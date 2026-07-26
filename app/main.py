from fastapi import FastAPI
from pydantic import BaseModel, Field

# --- IMPORTS DE BASE DE DATOS ---
from app.db import engine, Base
from app.models.sensor import SensorModel   
from app.models.reading import ReadingModel  

# --- CREAR TABLAS ---
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SensorHub API", version="0.1.0")
 
# 1. El "Contrato de Entrada" (Como el formato esperado de una trama UART)
class SensorReadingIn(BaseModel):
    sensor_id: str = Field(..., examples=["TEMP-01"])
    value: float
    unit: str = "C"
 
# 2. El "Contrato de Salida" (Lo que realmente emitimos de vuelta)
class SensorReadingOut(SensorReadingIn):
    id: int
 
# 3. Endpoint de salud: vital en despliegues reales (AWS, Render, Docker)
@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
 
# 4. Endpoint de creación de lecturas
@app.post("/readings", response_model=SensorReadingOut, status_code=201)
def create_reading(reading: SensorReadingIn) -> SensorReadingOut:
    # Por ahora "mockeamos" la base de datos asignando un ID fijo de 1.
    return SensorReadingOut(id=1, **reading.model_dump())