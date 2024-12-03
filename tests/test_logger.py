import unittest
from src.logger import log_packet, log_anomaly
import os

class TestLogging(unittest.TestCase):
    def test_logging(self):
        """
        Test logging of packets and anomalies.
        """
        log_file = "logs/system.log"
        if os.path.exists(log_file):
            os.remove(log_file)  # Clean log file before testing

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