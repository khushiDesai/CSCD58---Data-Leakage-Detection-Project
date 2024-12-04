import logging
import os
import unittest

project_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def ensure_log_directory():
    """
    Ensures the 'logs' directory exists. Creates it if it doesn't.
    """
    log_dir = os.path.join(project_root, "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

def check_file_exit():
    """
    Ensures the log file exists.
    """
    log_file = os.path.join(project_root, "logs", "system.log")
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            pass

ensure_log_directory()

# Configure logging settings
log_file_path = os.path.join(project_root, "logs", "system.log")
logging.basicConfig(
    filename=log_file_path,
    filemode='a',  # Append to file
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def flush_logs():
    """
    Flush the logging handlers to ensure logs are written to the file immediately.
    """
    for handler in logging.getLogger().handlers:
        handler.flush()

def log_packet(src, dst, size):
    """
    Logs details of a captured packet.
    """
    check_file_exit()
    logging.info(f"Packet: {src} -> {dst}, Size: {size}")
    flush_logs()

def log_anomaly(src, dst, size):
    """
    Logs details of a detected anomaly.
    """
    check_file_exit()
    logging.warning(f"Anomaly detected: {src} -> {dst}, Size: {size}")
    flush_logs()

# Integrated tests
class TestLogging(unittest.TestCase):
    def test_logging(self):
        """
        Test logging of packets and anomalies.
        """
        log_file = os.path.join(project_root, "logs", "system.log")

        # Ensure the log file exists
        if not os.path.exists(log_file):
            check_file_exit()

        # Clean the log file before testing
        if os.path.exists(log_file):
            os.remove(log_file)

        print("Testing packet logging...")
        log_packet("192.168.1.100", "10.0.0.1", 1500)
        log_anomaly("192.168.1.100", "10.0.0.1", 2000)

        # Check the log file for entries
        try:
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