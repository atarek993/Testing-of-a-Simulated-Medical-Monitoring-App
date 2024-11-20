

class EmergencyService:
    """Simulates contacting emergency services."""
    def __init__(self, hospital_contact, ambulance_contact):
        self.hospital_contact = hospital_contact
        self.ambulance_contact = ambulance_contact

    def contact_hospital(self):
        return f"Hospital contacted at {self.hospital_contact}."

    def dispatch_ambulance(self):
        return f"Ambulance dispatched to the location via {self.ambulance_contact}."
