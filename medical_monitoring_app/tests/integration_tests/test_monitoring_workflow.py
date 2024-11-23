import pytest
from app.monitoring_workflow import MedicalMonitoringApp

@pytest.fixture
def app(tmp_path):
    """
    Fixture to initialize the app with a temporary file for clean test runs.
    """
    app_instance = MedicalMonitoringApp(
        log_file=tmp_path / "test_logs.json",
        alert_file=tmp_path / "test_alerts.json"
    )
    app_instance.logger.clear_logs()  # Clear the logs before each test
    return app_instance

def test_monitor_patient_alerts(app):
    statuses = app.monitor_patient(heart_rate=120, blood_pressure=140, oxygen_saturation=88)
    assert len(statuses) == 3
    assert any("Alert" in status for status in statuses)
    assert len(app.get_alerts()) > 0

def test_logging_in_workflow(app):
    app.monitor_patient(heart_rate=70, blood_pressure=115, oxygen_saturation=96)
    biosignal_logs, alert_logs = app.logger.get_logs()
    assert len(biosignal_logs) > 0  # Biosignal logs should be present
    assert len(alert_logs) == 0  # No alerts expected

def test_boundary_values(app):
    statuses = app.monitor_patient(heart_rate=120, blood_pressure=140, oxygen_saturation=88)
    assert "Alert" in statuses[0]  # Boundary value for heart rate

def test_invalid_inputs(app):
    statuses = app.monitor_patient(heart_rate=None, blood_pressure=None, oxygen_saturation=None)
    assert "invalid input" in statuses[0]  # Handle invalid input gracefully

def test_high_load(app):
    for i in range(1000):  # Simulating high load
        app.monitor_patient(heart_rate=120, blood_pressure=140, oxygen_saturation=88)
    biosignal_logs, alert_logs = app.logger.get_logs()
    assert len(biosignal_logs) == 1000  # Ensure all biosignal entries were logged

def test_logging_behavior(app):
    app.monitor_patient(heart_rate=75, blood_pressure=120, oxygen_saturation=95)
    biosignal_logs, alert_logs = app.logger.get_logs()
    assert len(biosignal_logs) > 0  # Biosignal data should be logged

    app.monitor_patient(heart_rate=150, blood_pressure=180, oxygen_saturation=85)
    biosignal_logs, alert_logs = app.logger.get_logs()
    assert len(alert_logs) > 0  # Alert should be logged for abnormal values
