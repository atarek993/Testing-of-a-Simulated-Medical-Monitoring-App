from biosignals import *

class WearableDevice:
    """Simulates the wearable device."""
    def __init__(self):
        self.heart_rate = HeartRate()
        self.blood_pressure = BloodPressure()
        self.oxygen_saturation = OxygenSaturation()

    def read_signals(self, heart_rate, blood_pressure, oxygen_saturation):
        hr_status = self.heart_rate.update_value(heart_rate)
        bp_status = self.blood_pressure.update_value(blood_pressure)
        ox_status = self.oxygen_saturation.update_value(oxygen_saturation)
        return [hr_status, bp_status, ox_status]
