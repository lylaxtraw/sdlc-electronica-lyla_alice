from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool  # <-- NUEVO: Importar StaticPool

# Asegúrate de importar tu app y tus configuraciones de BD
from app.main import app
from app.db import Base, get_db

# <-- OPCIONAL PERO RECOMENDADO: Asegurar que Base conozca tus modelos antes de crear las tablas
# from app.models.reading import Reading 

# 1. Configurar un motor SQLite en memoria exclusivamente para los tests
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

# <-- NUEVO: Añadir poolclass=StaticPool al engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False},
    poolclass=StaticPool  
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. Crear las tablas en este motor en memoria (ahora persistirá para los tests)
Base.metadata.create_all(bind=engine)

# 3. Crear una función que reemplace a get_db
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# 4. Forzar a FastAPI a usar nuestra función de prueba en lugar de la original
app.dependency_overrides[get_db] = override_get_db

# 5. Inicializar el TestClient (ahora usará el motor en memoria)
client = TestClient(app)

# --- Tus pruebas de la API... ---
def test_health_endpoint():
    response = client.get("/health") 
    assert response.status_code == 200

def test_full_reading_lifecycle():
    # 1. Crear lectura (201 Created)
    create_res = client.post(
        "/sensors/TEMP-01/readings",
        json={"value": 23.5, "unit": "C"}
    )
    assert create_res.status_code == 201
    data = create_res.json()
    assert data["sensor_id"] == "TEMP-01"
    assert data["value"] == 23.5
    reading_id = data["id"]

    # 2. Consultar lectura individual por ID (200 OK)
    get_res = client.get(f"/readings/{reading_id}")
    assert get_res.status_code == 200
    assert get_res.json()["id"] == reading_id

    # 3. Listar lecturas paginadas (200 OK)
    list_res = client.get("/sensors/TEMP-01/readings?limit=10&offset=0")
    assert list_res.status_code == 200
    assert len(list_res.json()) == 1

    # 4. Actualizar parcialmente con PATCH (200 OK)
    patch_res = client.patch(
        f"/readings/{reading_id}",
        json={"value": 25.0}
    )
    assert patch_res.status_code == 200
    assert patch_res.json()["value"] == 25.0

    # 5. Intentar crear valor físico inválido (400 Bad Request)
    invalid_res = client.post(
        "/sensors/TEMP-01/readings",
        json={"value": -300.0, "unit": "C"}
    )
    assert invalid_res.status_code == 400

    # 6. Eliminar lectura (204 No Content)
    del_res = client.delete(f"/readings/{reading_id}")
    assert del_res.status_code == 204

    # 7. Verificar 404 Not Found al buscar la lectura eliminada
    not_found_res = client.get(f"/readings/{reading_id}")
    assert not_found_res.status_code == 404