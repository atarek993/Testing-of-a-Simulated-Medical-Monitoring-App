import pytest
from app.monitoring_workflow import MedicalMonitoringApp

def test_high_frequency_updates():
    app = MedicalMonitoringApp()
    for _ in range(10):  # Simulate 10 readings
        statuses = app.monitor_patient(heart_rate=80, blood_pressure=110, oxygen_saturation=98)
    assert statuses == [
        "Heart Rate is within safe range.",
        "Blood Pressure is within safe range.",
        "Oxygen Saturation is within safe range."
    ]

def test_high_load():
    app = MedicalMonitoringApp()
    for i in range(10):  # Simulating high load
        app.monitor_patient(heart_rate=120, blood_pressure=140, oxygen_saturation=88)
    # Validate performance doesn't degrade significantly

def test_slow_responses():
    app = MedicalMonitoringApp()
    app.set_network_delay(5)  # Simulate a 5-second delay
    statuses = app.monitor_patient(heart_rate=120, blood_pressure=140, oxygen_saturation=88)
    assert statuses is not None  # Check if the system can handle delays
