import logging
import os

def ensure_log_directory():
    """
    Ensures the 'logs' directory exists. Creates it if it doesn't.
    """
    
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src", "logs")
    
    # Check if the log directory exists, and create it if not
    if not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir)
            print(f"Created log directory: {log_dir}")
        except FileExistsError:
            # The directory was created by another process
            pass
    else:
        print(f"Log directory already exists: {log_dir}")

ensure_log_directory()

# Configure logging settings
logging.basicConfig(
    filename="src/logs/system.log",
    filemode='w', #overwrite file
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_packet(src, dst, size):
    print("logging")
    """
    Logs details of a captured packet.
    - src: Source IP address
    - dst: Destination IP address
    - size: Size of the packet in bytes
    """
    logging.info(f"Packet: {src} -> {dst}, Size: {size}")

def log_anomaly(src, dst, size):
    """
    Logs details of a detected anomaly.
    - src: Source IP address
    - dst: Destination IP address
    - size: Size of the packet in bytes
    """
    logging.warning(f"Anomaly detected: {src} -> {dst}, Size: {size}")