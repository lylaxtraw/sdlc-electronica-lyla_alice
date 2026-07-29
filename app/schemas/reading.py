# app/schemas/reading.py
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class ReadingCreate(BaseModel):
    value: float = Field(..., description="Valor medido por el sensor")
    unit: str = Field(..., max_length=10, description="Unidad de medida (ej. C, %)")

class ReadingUpdate(BaseModel):
    value: float | None = Field(None, description="Nuevo valor medido")
    unit: str | None = Field(None, max_length=10, description="Nueva unidad de medida")

class ReadingResponse(BaseModel):
    id: int
    sensor_id: str
    value: float
    unit: str
    created_at: datetime

    # Permite a Pydantic leer directamente instancias del ORM de SQLAlchemy
    model_config = ConfigDict(from_attributes=True)