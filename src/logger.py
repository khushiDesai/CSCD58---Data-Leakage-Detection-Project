import logging
import os
import unittest

# Resolve the absolute project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def ensure_log_directory():
    """
    Ensures the 'logs' directory exists. Creates it if it doesn't.
    """
    log_dir = os.path.join(project_root, "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

def get_log_file_path():
    """
    Returns the absolute path of the log file.
    """
    return os.path.join(project_root, "logs", "system.log")

ensure_log_directory()

# Configure logging settings
log_file_path = get_log_file_path()
logging.basicConfig(
    filename=log_file_path,
    filemode='w',  # Overwrite file for testing
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
    print(get_log_file_path())
    logging.info(f"Packet: {src} -> {dst}, Size: {size}")
    flush_logs()

def log_anomaly(src, dst, size):
    """
    Logs details of a detected anomaly.
    """
    logging.warning(f"Anomaly detected: {src} -> {dst}, Size: {size}")
    flush_logs()

# Integrated test
class TestLogging(unittest.TestCase):
    def test_logging(self):
        """
        Test logging of packets and anomalies.
        """
        log_file = get_log_file_path()

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
