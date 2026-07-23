# Bitácora de Inteligencia Artificial (AI_LOG.md)
**Herramienta utilizada:** Gemini 2.5 Pro

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

## Semana 1 · Entrada 4 (Jueves)
Prompt: "Completa la biblioteca en semana1/solid_isp_dip.py dividiendo una interfaz gorda en Readable, Writable y Calibratable (ISP), y usando Protocol para inyectar un DataRepository en un DataProcessor (DIP), junto con una implementación InMemoryRepository para pruebas"
La IA generó las estructuras de los protocolos y las clases de prueba sin alterar el fragmento base proporcionado en la guía. Acepté la implementación tras verificar línea por línea:
- Acepté la segregación de interfaces con `Protocol` (ISP), ya que evita que dispositivos de solo lectura como un ADC implementen métodos fantasma de calibración o escritura.
- Acepté el patrón de Inversión de Dependencias (DIP) y la clase `InMemoryRepository`. Comprobé que al inyectar la dependencia vía parámetro en `DataProcessor`, podemos testear toda la lógica de procesamiento en memoria RAM en milisegundos sin depender de conexiones a bases de datos externas.
- Acepté los 4 tests unitarios elaborados en `test_solid_isp_dip.py` tras validar que pasan limpiamente en pytest y cubren tanto el éxito como el manejo de lecturas inexistentes (`None`).

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

## Semana 1 · Entrada 4 (Jueves)
Prompt: "Completa la biblioteca en semana1/solid_isp_dip.py dividiendo una interfaz gorda en Readable, Writable y Calibratable (ISP), y usando Protocol para inyectar un DataRepository en un DataProcessor (DIP), junto con una implementación InMemoryRepository para pruebas"
La IA generó las estructuras de los protocolos y las clases de prueba sin alterar el fragmento base proporcionado en la guía. Acepté la implementación tras verificar línea por línea:
- Acepté la segregación de interfaces con `Protocol` (ISP), ya que evita que dispositivos de solo lectura como un ADC implementen métodos fantasma de calibración o escritura.
- Acepté el patrón de Inversión de Dependencias (DIP) y la clase `InMemoryRepository`. Comprobé que al inyectar la dependencia vía parámetro en `DataProcessor`, podemos testear toda la lógica de procesamiento en memoria RAM en milisegundos sin depender de conexiones a bases de datos externas.
- Acepté los 4 tests unitarios elaborados en `test_solid_isp_dip.py` tras validar que pasan limpiamente en pytest y cubren tanto el éxito como el manejo de lecturas inexistentes (`None`).

## Semana 1 · Entrada 5 (Viernes)
Prompt: "Genera el código y los tests para el driver UART modular (config, parsers, device, recorder) aplicando principios SOLID según las firmas especificadas en la guía del curso"
La IA propuso inicialmente una arquitectura con extensiones complejas (como buffers circulares por mutex y loggers JSON) que se desviaban de los archivos requeridos en la especificación. Rechacé la primera propuesta y obligué a una alineación estricta, detectando además un bug crítico en la lógica de evaluación. Igualmente, modifiqué los tests otorgados para separarlos y aplicarles una mejor estructura:
- **Rechacé el sobre-diseño arquitectónico:** Reduje el alcance para implementar únicamente los 4 archivos dictados por la guía (`config.py`, `parsers.py`, `device.py`, `recorder.py`).
- **Rechacé y corregí el comportamiento de `can_parse()` en `ModbusParser`:** La IA sugirió lanzar una excepción (`raise ValueError`) si la trama era corta. Esto violaba el Principio de Sustitución de Liskov (LSP) y Abierto/Cerrado (OCP), ya que colgaría la tubería de análisis completa si un coordinador tuviera múltiples parsers en cadena. Lo corregí para retornar `False`.
- **Acepté las firmas de los 12 tests unitarios básicos** tras comprobar que cubren los criterios mínimos exigidos (baudrates inválidos, inmutabilidad y persistencia).

****

## Semana 2 · Entrada 1 (Lunes)
Prompt: "Ayúdame a completar mis notas de la Scrum Guide 2020 con los 5 eventos y sus timeboxes, los 3 artefactos con sus compromisos, los 5 valores y la diferencia entre Definition of Done y Criterio de Aceptación, manteniendo estrictamente mi estilo de escritura y terminología en inglés"
La IA propuso el bloque de texto exacto para insertar en mi archivo Markdown, respetando el formato de viñetas y sin agregar burocracia innecesaria. Acepté las definiciones teóricas pero aclaramos la arquitectura de integración del tablero ágil:
- **Acepté la conceptualización técnica de los artefactos y sus compromisos asociados** (Product Goal, Sprint Goal y Definition of Done), así como la distinción clara entre DoD como estándar global de calidad para todo el producto y Criterio de Aceptación como condición funcional específica en Gherkin para una sola User Story.
- **Rechacé la duda inicial de crear el GitHub Project como un proyecto o repositorio aislado:** Tras analizar la diferencia arquitectónica entre un repositorio de código (Repo - control de versiones e historial inmutable) y un tablero ágil (Project - capa de gestión visual superpuesta al SDLC), determiné con criterio propio que integrarlo dentro del mismo repositorio es la mejor práctica en la industria para vincular de forma nativa los Issues con los futuros Pull Requests.

## Semana 2 · Entrada 2 (Martes)
Prompt: "Audita como un ingeniero implacable mi borrador de 7 User Stories con escenarios Gherkin para un sistema de monitoreo IoT de bodega industrial. Señala ambigüedades, casos borde olvidados para TDD y ayúdame a reestructurar el backlog hasta superar las 10 historias con priorización MoSCoW y Story Points en escala Fibonacci"
La IA propuso una auditoría técnica profunda que expuso varios fallos de diseño en mi borrador inicial y sugirió reestructurar el Product Backlog a 11 historias. Acepté las correcciones arquitectónicas y ajusté los límites de frontera para el diseño de pruebas:
- **Acepté la corrección del rol del actor**, cambiando "Como desarrolladora..."por usuarios funcionales de negocio ("Como administradora de bodega"), ya que en el SDLC el software se construye para aportar valor operativo en tiempo de ejecución, no para quien escribe el código.
- **Acepté la eliminación de "cadenas mágicas"** (Magic Strings, como hardcodear el ID "GHOST_99" en las pruebas) por condiciones dinámicas de inventario, y la integración de la historia US-08 para aplicar el patrón Strategy en el AlertManager (salida dual a consola y archivo) exigido por la rúbrica.
- **Rechacé y corregí el comportamiento de mi diseño inicial en la US-03**, donde indicaba abrir el log de problemas en "modo lectura". Arquitectónicamente, ante una excepción o superación del límite de sensores, el sistema debe escribir en la bitácora (modo append), no leerla.
- **Corregí la ambigüedad en los umbrales de temperatura y humedad para habilitar un TDD estricto**, definiendo explícitamente el comportamiento en las fronteras matemáticas (qué ocurre exactamente a los 35.0 °C) e introduciendo un caso borde de física imposible (-5 K) en la US-05 para verificar el manejo robusto de excepciones de dominio.

## Semana 2 · Entrada 3 (Miércoles)
Prompt: "Guíame paso a paso para implementar SensorRegistry, AnomalyDetector y AlertManager siguiendo un ciclo TDD estricto (Red-Green-Refactor), aplicando inyección de dependencias para umbrales y el patrón Strategy para las alertas"
La IA propuso los ciclos atómicos de prueba y código para cada componente, asegurando que las pruebas fallaran primero (RED) antes de implementar la lógica mínima (GREEN). Acepté la estructura pero realicé ajustes operativos en el entorno:
- **Acepté el diseño arquitectónico:** Validé el uso de inyección de dependencias en `AnomalyDetector` (evitando hardcodear 35.0 °C o 80.0 %) y el patrón Strategy mediante `Protocol` en `AlertManager`. Esto me permitió alcanzar un 99% de cobertura en las pruebas automatizadas.
- **Rechacé y corregí el flujo de ejecución de pruebas:** Al inicio, la ejecución directa de `pytest` falló arrojando un `ModuleNotFoundError`. Analicé que el `PYTHONPATH` no estaba resolviendo la raíz del proyecto; lo corregí creando los archivos `__init__.py` necesarios y adoptando el comando estándar `python -m pytest` para todo el ciclo.
- **Corregí hallazgos de análisis estático en el Refactor:** Durante los ciclos en verde, ejecuté `ruff check` y detecté importaciones huérfanas introducidas por los ejemplos de la IA (como un `import pytest` sin uso en `test_detector.py`). Acepté el fallo del linter y limpié las dependencias antes de sellar el commit de refactorización.

## Semana 2 · Entrada 4 (Jueves)
Prompt: "Ayúdame a redactar la Definition of Done estricta, configurar pyproject.toml para automatizar la calidad (cobertura >= 80%, ruff, mypy) y generar los artefactos Scrum finales (Sprint Planning y Retrospective) basados en nuestro historial"
La IA generó el contrato en `DEFINITION_OF_DONE.md`, el archivo de configuración para centralizar las reglas de validación en Python, y los textos de los artefactos Scrum, sugiriendo integrar los cambios mediante ramas. Acepté la implementación tras verificar su impacto en el proyecto:
- **Acepté la automatización del contrato de calidad:** Validé la configuración en `pyproject.toml` (`--cov-fail-under=80`, `strict=true` para mypy). Reflexioné que como ingeniero es ineficiente auditar estilos o cobertura a mano; delegar estas reglas a un sistema automatizado (CI local) asegura que los tests fallen si se viola la DoD.
- **Acepté la integración mediante flujo Git profesional:** Adopté la recomendación de encapsular la configuración en una rama aislada (`feature/config-dod`) y simular un Pull Request local hacia `main`. Aunque trabajo solo, esto mantiene un historial limpio y respeta el estándar corporativo.
- **Validé los artefactos Scrum con criterio propio:** Revisé el *Sprint Planning* asegurando que las tareas mantuvieran el rigor heurístico de $\le 4$ horas, y definí en la *Retrospectiva* una acción de mejora real: implementar un checklist de *scaffolding* para prevenir los problemas de entorno (`ModuleNotFoundError`) sufridos el día anterior.