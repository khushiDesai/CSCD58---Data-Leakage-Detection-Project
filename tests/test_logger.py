import unittest
import os
from src.logger import log_packet, log_anomaly

def ensure_log_file(log_file):
    """
    Ensures the log directory and file exist.
    """
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            pass

class TestLogging(unittest.TestCase):
    def test_logging(self):
        """
        Test logging of packets and anomalies.
        """
        log_file = os.path.join(os.path.dirname(__file__), "../logs/system.log")
        log_file = os.path.abspath(log_file)
        ensure_log_file(log_file)

        print(f"Current working directory: {os.getcwd()}")
        print(f"Resolved log file path: {log_file}")

        # Attempt to clean the log file before testing
        if os.path.exists(log_file):
            try:
                os.remove(log_file)
            except PermissionError as e:
                self.fail(f"PermissionError: Unable to remove log file: {e}")

        print("Testing packet logging...")
        log_packet("192.168.1.100", "10.0.0.1", 1500)
        log_anomaly("192.168.1.100", "10.0.0.1", 2000)

        # Check the log file for entries
        with open(log_file, "r") as f:
            logs = f.read()
            self.assertIn("Packet: 192.168.1.100 -> 10.0.0.1, Size: 1500", logs)
            self.assertIn("Anomaly detected: 192.168.1.100 -> 10.0.0.1, Size: 2000", logs)

if __name__ == "__main__":
    unittest.main()