# app/routers/readings.py
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.reading_repo import SQLAlchemyReadingRepository
from app.services.reading_service import ReadingService
from app.schemas.reading import ReadingCreate, ReadingUpdate, ReadingResponse

router = APIRouter(tags=["Readings"])

# Fábrica de servicio inyectable mediante Depends
def get_reading_service(db: Session = Depends(get_db)) -> ReadingService:
    repo = SQLAlchemyReadingRepository(db)
    return ReadingService(repo)

# 1. POST /sensors/{sensor_id}/readings (201 Created)
@router.post(
    "/sensors/{sensor_id}/readings",
    response_model=ReadingResponse,
    status_code=status.HTTP_201_CREATED
)
def create_reading(
    sensor_id: str,
    payload: ReadingCreate,
    service: ReadingService = Depends(get_reading_service)
):
    try:
        return service.record(sensor_id, payload.value, payload.unit)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

# 2. GET /sensors/{sensor_id}/readings (200 OK con Paginación y Filtros de Fecha)
@router.get(
    "/sensors/{sensor_id}/readings",
    response_model=list[ReadingResponse],
    status_code=status.HTTP_200_OK
)
def list_readings(
    sensor_id: str,
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
    from_date: datetime | None = Query(None, alias="from"),
    to_date: datetime | None = Query(None, alias="to"),
    service: ReadingService = Depends(get_reading_service)
):
    try:
        return service.list_readings(sensor_id, limit, offset, from_date, to_date)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

# 3. GET /readings/{id} (200 OK)
@router.get(
    "/readings/{reading_id}",
    response_model=ReadingResponse,
    status_code=status.HTTP_200_OK
)
def get_reading(
    reading_id: int,
    service: ReadingService = Depends(get_reading_service)
):
    reading = service.get_reading(reading_id)
    if not reading:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lectura con ID {reading_id} no encontrada"
        )
    return reading

# 4. PATCH /readings/{id} (200 OK)
@router.patch(
    "/readings/{reading_id}",
    response_model=ReadingResponse,
    status_code=status.HTTP_200_OK
)
def update_reading(
    reading_id: int,
    payload: ReadingUpdate,
    service: ReadingService = Depends(get_reading_service)
):
    try:
        updated = service.update_reading(reading_id, payload.value, payload.unit)
        if not updated:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Lectura con ID {reading_id} no encontrada"
            )
        return updated
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

# 5. DELETE /readings/{id} (204 No Content)
@router.delete(
    "/readings/{reading_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_reading(
    reading_id: int,
    service: ReadingService = Depends(get_reading_service)
):
    deleted = service.delete_reading(reading_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lectura con ID {reading_id} no encontrada"
        )
    return None