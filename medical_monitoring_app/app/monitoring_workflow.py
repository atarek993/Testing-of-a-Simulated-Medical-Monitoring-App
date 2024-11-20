from device import WearableDevice
from emergency_service import EmergencyService
from data_logger import DataLogger
from datetime import datetime

class MedicalMonitoringApp:
    """Main app logic."""

    def __init__(self):
        self.device = WearableDevice()
        self.emergency_service = EmergencyService("123-456-789", "987-654-321")
        self.alerts = []
        self.logger = DataLogger()  # Integrating DataLogger for logging biosignals and alerts

    def monitor_patient(self, heart_rate, blood_pressure, oxygen_saturation):
        # Read signals
        statuses = self.device.read_signals(heart_rate, blood_pressure, oxygen_saturation)
        
        # Log biosignal data
        timestamp = datetime.now().isoformat()
        biosignal_data = {
            "heart_rate": heart_rate,
            "blood_pressure": blood_pressure,
            "oxygen_saturation": oxygen_saturation,
            "statuses": statuses
        }
        self.logger.log_biosignal(timestamp, biosignal_data)

        # Filter and handle alerts
        self.alerts = [status for status in statuses if "Alert" in status]
        if self.alerts:
            self.handle_emergency(timestamp)

        return statuses

    def handle_emergency(self, timestamp):
        # Simplified emergency handling
        hospital_alert = self.emergency_service.contact_hospital()
        ambulance_alert = self.emergency_service.dispatch_ambulance()

        self.alerts.extend([hospital_alert, ambulance_alert])

        # Log alerts
        for alert in [hospital_alert, ambulance_alert]:
            self.logger.log_alert(timestamp, alert)

    def get_alerts(self):
        return self.alerts


if __name__ == "__main__":
    app = MedicalMonitoringApp()

    # Simulated patient monitoring
    statuses = app.monitor_patient(heart_rate=120, blood_pressure=140, oxygen_saturation=88)
    print("Monitoring Statuses:")
    print("\n".join(statuses))

    alerts = app.get_alerts()
    print("\nAlerts:")
    print("\n".join(alerts))

    # Display logs (for demonstration purposes)
    biosignal_logs, alert_logs = app.logger.get_logs()
    print("\nBiosignal Logs:")
    print(biosignal_logs)
    print("\nAlert Logs:")
    print(alert_logs)
