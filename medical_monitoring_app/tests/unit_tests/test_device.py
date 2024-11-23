import pytest
from app.device import WearableDevice

def test_wearable_device_signals():
    device = WearableDevice()
    statuses = device.read_signals(heart_rate=120, blood_pressure=130, oxygen_saturation=90)
    assert "Alert: Heart Rate out of safe range!" in statuses
    assert "Alert: Blood Pressure out of safe range!" in statuses
    assert "Alert: Oxygen Saturation out of safe range!" in statuses
