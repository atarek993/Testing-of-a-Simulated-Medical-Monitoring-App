import pytest
from app.emergency_service import EmergencyService

def test_contact_hospital():
    service = EmergencyService("123-456-789", "987-654-321")
    assert service.contact_hospital() == "Hospital contacted at 123-456-789."

def test_dispatch_ambulance():
    service = EmergencyService("123-456-789", "987-654-321")
    assert service.dispatch_ambulance() == "Ambulance dispatched to the location via 987-654-321."
