import pytest
import os
import json
from app.data_logger import DataLogger

@pytest.fixture
def logger(tmp_path):
    return DataLogger(
        log_file=tmp_path / "test_logs.json",
        alert_file=tmp_path / "test_alerts.json"
    )

def test_initialize_files(logger):
    assert os.path.exists(logger.log_file)
    assert os.path.exists(logger.alert_file)

def test_log_biosignal(logger):
    logger.log_biosignal("2024-01-01T00:00:00", {"heart_rate": 85})
    with open(logger.log_file, "r") as f:
        data = json.load(f)
    assert data[0]["data"]["heart_rate"] == 85

def test_log_alert(logger):
    logger.log_alert("2024-01-01T00:00:00", "Test alert")
    with open(logger.alert_file, "r") as f:
        data = json.load(f)
    assert data[0]["alert"] == "Test alert"
