import pytest
from app.biosignals import HeartRate, BloodPressure, OxygenSaturation

def test_heart_rate_within_range():
    hr = HeartRate()
    assert hr.update_value(80) == "Heart Rate is within safe range."

def test_heart_rate_above_range():
    hr = HeartRate()
    assert hr.update_value(110) == "Alert: Heart Rate out of safe range!"

def test_blood_pressure_below_range():
    bp = BloodPressure()
    assert bp.update_value(75) == "Alert: Blood Pressure out of safe range!"

def test_oxygen_saturation_edge_case():
    ox = OxygenSaturation()
    assert ox.update_value(95) == "Oxygen Saturation is within safe range."
    assert ox.update_value(94) == "Alert: Oxygen Saturation out of safe range!"
