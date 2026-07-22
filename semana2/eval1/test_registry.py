import pytest
from semana2.eval1.registry import SensorRegistry, SensorNotFoundError


def test_get_unknown_sensor_raises() -> None:
    registry = SensorRegistry()
    with pytest.raises(SensorNotFoundError):
        registry.get("TEMP_99")