from app.device import WearableDevice
from app.emergency_service import EmergencyService
from app.data_logger import DataLogger
from datetime import datetime

class MedicalMonitoringApp:
    """Main app logic."""

    def __init__(self, log_file="biosignal_logs.json", alert_file="alerts.json"):
        """
        Initializes the app with optional paths for log and alert files.
        
        Args:
            log_file (str): Path to the file for storing biosignal data.
            alert_file (str): Path to the file for storing alert logs.
        """
        self.device = WearableDevice()
        self.emergency_service = EmergencyService("123-456-789", "987-654-321")
        self.alerts = []
        # Initialize the logger with the provided log and alert file paths
        self.logger = DataLogger(log_file=log_file, alert_file=alert_file)

    def monitor_patient(self, heart_rate, blood_pressure, oxygen_saturation):
        """
        Monitor patient vitals, log biosignal data, and handle emergencies if needed.
        """
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
        if self.alerts:  # Only handle emergency if there are alerts
            self.handle_emergency(timestamp)

        return statuses

    def handle_emergency(self, timestamp):
        """
        Handle emergencies by contacting hospital and dispatching ambulance only when alerts exist.
        """
        if not self.alerts:  # Prevent unnecessary emergency handling
            return

        # Contact emergency services only when there are alerts
        hospital_alert = self.emergency_service.contact_hospital()
        ambulance_alert = self.emergency_service.dispatch_ambulance()

        # Add these alerts to the list
        self.alerts.extend([hospital_alert, ambulance_alert])

        # Log these alerts
        for alert in [hospital_alert, ambulance_alert]:
            self.logger.log_alert(timestamp, alert)

    def get_alerts(self):
        """
        Retrieve the list of alerts triggered during monitoring.
        """
        return self.alerts

# Example usage:
if __name__ == "__main__":
    app = MedicalMonitoringApp(log_file="test_logs.json", alert_file="test_alerts.json")

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
