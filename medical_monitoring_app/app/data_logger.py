import json
import os
from datetime import datetime

class DataLogger:
    """
    A class responsible for logging biosignal data, alerts, and critical events.
    """

    def __init__(self, log_file="biosignal_logs.json", alert_file="alerts.json"):
        """
        Initializes the logger with default or provided file paths.
        
        Args:
            log_file (str): Path to the file for storing biosignal data.
            alert_file (str): Path to the file for storing alert logs.
        """
        self.log_file = log_file
        self.alert_file = alert_file
        self._initialize_files()

    def _initialize_files(self):
        """
        Ensures the log files exist; creates empty ones if they don't.
        """
        for file in [self.log_file, self.alert_file]:
            if not os.path.exists(file):
                with open(file, "w") as f:
                    json.dump([], f)

    def log_biosignal(self, timestamp, biosignal_data):
        """
        Logs biosignal data to the data log file.

        Args:
            timestamp (str): The time the data was recorded.
            biosignal_data (dict): Dictionary containing biosignal information.
        """
        log_entry = {
            "timestamp": timestamp,
            "data": biosignal_data
        }
        self._write_to_file(self.log_file, log_entry)

    def log_alert(self, timestamp, alert_message):
        """
        Logs alert messages to the alert log file.

        Args:
            timestamp (str): The time the alert was triggered.
            alert_message (str): Description of the alert.
        """
        alert_entry = {
            "timestamp": timestamp,
            "alert": alert_message
        }
        self._write_to_file(self.alert_file, alert_entry)

    def _write_to_file(self, file_path, entry):
        """
        Appends an entry to a JSON file.

        Args:
            file_path (str): Path to the file.
            entry (dict): The data to be logged.
        """
        with open(file_path, "r+") as f:
            data = json.load(f)
            data.append(entry)
            f.seek(0)
            json.dump(data, f, indent=4)

    def get_logs(self):
        """
        Retrieves all biosignal and alert logs.

        Returns:
            tuple: A tuple containing lists of biosignal logs and alert logs.
        """
        with open(self.log_file, "r") as biosignal_file:
            biosignal_logs = json.load(biosignal_file)

        with open(self.alert_file, "r") as alert_file:
            alert_logs = json.load(alert_file)

        return biosignal_logs, alert_logs

# Example usage:
if __name__ == "__main__":
    logger = DataLogger()
    timestamp = datetime.now().isoformat()

    # Log some biosignal data
    biosignal_data = {
        "heart_rate": 75,
        "oxygen_saturation": 98,
        "blood_pressure": "120/80"
    }
    logger.log_biosignal(timestamp, biosignal_data)

    # Log an alert
    alert_message = "Heart rate exceeds safe threshold!"
    logger.log_alert(timestamp, alert_message)

    # Fetch and print logs
    biosignal_logs, alert_logs = logger.get_logs()
    print("Biosignal Logs:", biosignal_logs)
    print("Alert Logs:", alert_logs)
