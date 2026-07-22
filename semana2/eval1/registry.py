class SensorNotFoundError(Exception):
    """Se lanza cuando se consulta un sensor no registrado en el sistema."""
    pass


class SensorRegistry:
    def __init__(self) -> None:
        self._sensors: dict[str, str] = {}

    def get(self, sensor_id: str) -> str:
        if sensor_id not in self._sensors:
            raise SensorNotFoundError(f"El sensor '{sensor_id}' no está registrado.")
        return self._sensors[sensor_id]