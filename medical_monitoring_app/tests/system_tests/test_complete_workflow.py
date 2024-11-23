from app.monitoring_workflow import MedicalMonitoringApp

def test_end_to_end_workflow():
    app = MedicalMonitoringApp()
    statuses = app.monitor_patient(heart_rate=65, blood_pressure=115, oxygen_saturation=97)
    assert all("within safe range" in status for status in statuses)
    alerts = app.get_alerts()
    assert len(alerts) == 0  # No alerts expected
