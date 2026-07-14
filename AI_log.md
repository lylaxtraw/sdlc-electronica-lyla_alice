# Bitácora de Inteligencia Artificial (AI_LOG.md)

## [2026-07-13] - Lunes Semana 1: Python idiomático y modelado de sensores
- **Contexto / Tarea:** Mapear conceptos de hardware/C a Python moderno, creando estructuras para lecturas de sensores (`Reading`) y procesamiento puro sin efectos secundarios.
- **Cómo ayudó la IA:** Generó la estructura base con `@dataclass(frozen=True)`, `Enum` y `Protocol`, además de las 5 funciones puras en `sensor_utils.py`.
- **Auditoría humana y aprendizaje:**
  - Entendí que `frozen=True` reemplaza el manejo cauteloso de punteros por inmutabilidad nativa, evitando que variables de estado cambien por error en otras funciones (cero efectos secundarios).
  - Aprendí la diferencia de tipado estructural (`Protocol`) vs herencia tradicional: en Python no necesito heredar de `Sensor` si implemento sus métodos (Duck Typing tipado).
  - Aprendí que las herramientas de análisis estático (`mypy`, `ruff`) siempre deben correrse desde el directorio raíz del proyecto para que los imports absolutos funcionen correctamente.