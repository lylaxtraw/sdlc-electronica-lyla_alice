# app/main.py
from fastapi import FastAPI
from app.db import engine, Base
from app.models import SensorModel, ReadingModel
from app.routers.readings import router as readings_router

# Inicializar tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SensorHub API",
    description="API RESTful para monitoreo de sensores industriales",
    version="0.1.0"
)

# Incluir las rutas modulares
app.include_router(readings_router)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}