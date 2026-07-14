# Bitácora de Inteligencia Artificial (AI_LOG.md)

## Semana 1 · Entrada 1 (Lunes)
Prompt: "Mapea una lectura de sensor de C a Python moderno usando dataclasses inmutables, enums, tipado estructural (Protocol) y 5 funciones puras de procesamiento"
La IA propuso la estructura `Reading` con `@dataclass(frozen=True)`, el protocolo `Sensor` y las 5 funciones en `sensor_utils.py`. Acepté el código pero ajusté el flujo de validación:
- Acepté el modelado de datos y la sintaxis de reemplazo inmutable (`dataclasses.replace`), ya que elimina efectos secundarios comunes en punteros de C.
- Rechacé la forma inicial de ejecutar `mypy` desde dentro de la subcarpeta `semana1/` porque lanzaba errores de resolución de módulos. Lo corregí ejecutando las herramientas de auditoría siempre desde el directorio raíz del proyecto.

## Semana 1 · Entrada 2 (Martes)
Prompt: "Reimplementa una máquina de estados finita (FSM) orientada a objetos para experimentar el estilo OO frente al C procedural, con 4 tests unitarios"
La IA propuso inicialmente una FSM para un nodo IoT de sensores con manejo de excepciones complejas. Rechacé la primera propuesta y acepté la corrección:
- Rechacé el modelo de FSM IoT porque se desviaba de la especificación estricta de la guía, la cual pedía un semáforo (`TrafficLightFSM`).
- Acepté la segunda implementación con `TrafficLightState` y el uso de un diccionario para mapear las transiciones O(1) en lugar de un switch-case procedural.
- Acepté los 4 tests unitarios de `test_fsm.py` tras verificar que probaban exactamente los escenarios exigidos: estado inicial, transición RED->GREEN, ciclo completo y conteo de ciclos.

## Semana 1 · Entrada 3 (Miércoles)
Prompt: "Implementa los tres primeros principios SOLID (S, O y L) con el código base y las firmas exactas indicadas en la guía para SensorReader, AlertStrategy, AnomalyDetector y process_sensor"
La IA propuso inicialmente una versión sobre-diseñada (over-engineered) que renombraba métodos (como `process_sensor_data`), cambiaba firmas de clases e ignoraba las interfaces explícitas entregadas en la guía. Rechacé esa primera propuesta y exigí una corrección estricta:
- Rechacé la modificación de firmas y el renombramiento de clases base. En arquitectura de software, alterar un contrato preestablecido rompe la compatibilidad e invalida pruebas automatizadas de integración.
- Acepté la implementación corregida tras auditar que preservaba intacto el fragmento de la guía (`AlertStrategy`, `AnomalyDetector`, `process_sensor`), limitándose únicamente a construir las clases derivadas (`ConsoleAlert`, `FileAlert`, `TemperatureSensor`, `HumiditySensor`) y los ejemplos de contraste "mal/bien".
- Acepté los 6 tests unitarios correspondientes (2 por cada principio) tras verificar su paso exitoso en pytest.