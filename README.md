# sdlc-electronica-lyla_alice
## **Semana 1: UART driver**
Este módulo contiene la reimplementación de un driver UART de estilo embebido (tradicionalmente procedural, acoplado y dependiente de estados globales en C) transformado en una arquitectura modular, orientada a objetos y estrictamente tipada en Python moderno.

El diseño se enfoca en eliminar buffers globales y el acoplamiento de protocolos, facilitando la instanciación múltiple del dispositivo y permitiendo pruebas unitarias en aislamiento total del hardware físico.

## Estructura del Módulo

La arquitectura está completamente segregada bajo los principios SOLID, dividiéndose en los siguientes componentes esenciales:

* **`config.py` (Principio de Responsabilidad Única - SRP):** Contiene la clase `UartConfig` diseñada como una `dataclass` inmutable (`frozen=True`). Se encarga exclusivamente de encapsular y validar en su construcción los parámetros del puerto (baudrate estándar, paridad y bits de parada), lanzando excepciones controladas si los parámetros de hardware son inválidos.
* **`parsers.py` (Principios OCP, LSP e ISP):** Define el contrato abstracto `MessageParser` mediante una clase base (`ABC`). Las implementaciones concretas (`ModbusParser` para tramas binarias RTU y `NMEAParser` para sentencias de texto GPS `$GPGGA`) extienden este contrato mediante polimorfismo, permitiendo que la tubería de análisis inspeccione y procese datos sin modificar la lógica base.
* **`device.py` (Principio de Inversión de Dependencias - DIP):** Implementa la clase `UartDevice`. El dispositivo no instancia internamente sus configuraciones ni hardcodea el protocolo; en su lugar, recibe la abstracción de `UartConfig` y `MessageParser` a través de **Inyección de Dependencias** en el constructor. Incluye un buffer de recepción simulado para pruebas en entornos sin hardware real.
* **`recorder.py` (Principio de Responsabilidad Única - SRP):** Clase `DataRecorder` dedicada únicamente a la persistencia en almacenamiento local de los datos procesados. Guarda la información estructurada utilizando el formato estándar **JSON-lines (`.jsonl`)**, donde cada registro es una línea independiente autodescriptiva.

---

## Instalación y Configuración del Entorno

Para configurar el entorno de ejecución profesional y garantizar el aislamiento de las dependencias, siga estos pasos desde el directorio raíz del repositorio:

1.  **Crear el entorno virtual aislado:**
    ```bash
    python3 -m venv .venv
    ```

2.  **Activar el entorno virtual:**
    * En macOS y Linux:
        ```bash
        source .venv/bin/activate
        ```
    * En Windows (Git Bash / WSL):
        ```bash
        source .venv/Scripts/activate
        ```

3.  **Instalar las herramientas de desarrollo y dependencias del ecosistema:**
    ```bash
    pip install pytest pytest-cov ruff mypy fastapi uvicorn sqlalchemy alembic httpx
    ```

---

## Ejecución de la Suite de Pruebas y Auditoría Estática

La verificación del comportamiento y la calidad del código se ejecuta de manera centralizada desde el **directorio raíz del repositorio** utilizando la santísima trinidad de herramientas de análisis en Python:

### 1. Pruebas Unitarias Automatizadas (`pytest`)
Para correr el set completo de pruebas unitarias (los 12 escenarios mínimos distribuidos entre las clases de configuración, parsers, ciclo de vida del dispositivo y persistencia en archivos):
```bash
pytest semana1/ -v
```

---
