import unittest
import os
from src.logger import log_packet, log_anomaly

def ensure_log_file(log_file):
    """
    Ensures the log directory and file exist.
    """
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
    log_file = os.path.join(log_dir, "system.log")
    log_file = os.path.abspath(log_file)

    try:
        # Create the directory if it does not exist
        if not os.path.exists(log_dir):
            print(f"Creating log directory: {log_dir}")
            os.makedirs(log_dir)
        
        # Create the file if it does not exist
        if not os.path.exists(log_file):
            print(f"Creating log file: {log_file}")
            with open(log_file, "w") as f:
                pass
    except Exception as e:
        raise RuntimeError(f"Error ensuring log file '{log_file}': {e}")

class TestLogging(unittest.TestCase):
    def test_logging(self):
        """
        Test logging of packets and anomalies.
        """
        log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "system.log")
        log_file = os.path.abspath(log_file)
        
        # Ensure the log file exists
        # ensure_log_file(log_file)


        # Attempt to clean the log file before testing
        try:
            if os.path.exists(log_file):
                os.remove(log_file)
        except PermissionError as e:
            self.fail(f"PermissionError: Unable to remove log file: {e}")
        except Exception as e:
            self.fail(f"Unexpected error while removing log file: {e}")

        print("Testing packet logging...")
        log_packet("192.168.1.100", "10.0.0.1", 1500)
        log_anomaly("192.168.1.100", "10.0.0.1", 2000)

        # Check the log file for entries
        try:
            print(log_file)
            with open(log_file, "r") as f:
                logs = f.read()
                print("Log file contents:")
                print(logs)
                self.assertIn("Packet: 192.168.1.100 -> 10.0.0.1, Size: 1500", logs)
                self.assertIn("Anomaly detected: 192.168.1.100 -> 10.0.0.1, Size: 2000", logs)
        except FileNotFoundError:
            self.fail(f"Log file '{log_file}' was not found after logging operations.")
        except Exception as e:
            self.fail(f"Unexpected error reading log file: {e}")

if __name__ == "__main__":
    unittest.main()