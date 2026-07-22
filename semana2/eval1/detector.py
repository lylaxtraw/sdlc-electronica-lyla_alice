from semana2.eval1.models import SensorReading


class AnomalyDetector:
    def __init__(self, max_temperature: float, max_humidity: float) -> None:
        self.max_temp = max_temperature
        self.max_hum = max_humidity

    def is_anomaly(self, reading: SensorReading) -> bool:
        if reading.category == "TEMPERATURE" and reading.value > self.max_temp:
            return True
        return False

    def get_anomaly_type(self, reading: SensorReading) -> str:
        if reading.category == "TEMPERATURE" and reading.value > self.max_temp:
            return "TEMP_THRESHOLD_BREACHED"
        return "NORMAL"