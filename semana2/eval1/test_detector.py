import pytest
from semana2.eval1.models import SensorReading
from semana2.eval1.detector import AnomalyDetector


def test_temperature_anomaly_detected_above_threshold() -> None:
    # Inyectamos el umbral de 35.0 °C al detector
    detector = AnomalyDetector(max_temperature=35.0, max_humidity=80.0)
    
    # Creamos una lectura que supera el umbral
    reading = SensorReading(sensor_id="TEMP_01", value=36.5, category="TEMPERATURE")
    
    assert detector.is_anomaly(reading) is True
    assert detector.get_anomaly_type(reading) == "TEMP_THRESHOLD_BREACHED"