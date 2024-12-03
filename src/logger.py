import logging
import os

def ensure_log_directory():
    """
    Ensures the 'logs' directory exists. Creates it if it doesn't.
    """
    
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src", "logs")

    log_file = os.path.join(log_dir, "system.log")
    log_file = os.path.abspath(log_file)
    # Check if the log directory exists, and create it if not
    if not os.path.exists(log_file):
        try:
            print(f"Created log file: {log_file}")
            with open(log_file, "w") as f:
                pass
            
        except FileExistsError:
            # The directory was created by another process
            pass
    else:
        print(f"Log directory file already exists: {log_dir}")

# Configure logging settings
logging.basicConfig(
    filename="src/logs/system.log",
    filemode='w', #overwrite file
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_packet(src, dst, size):
    """
    Logs details of a captured packet.
    - src: Source IP address
    - dst: Destination IP address
    - size: Size of the packet in bytes
    """
    ensure_log_directory()
    logging.info(f"Packet: {src} -> {dst}, Size: {size}")

def log_anomaly(src, dst, size):
    """
    Logs details of a detected anomaly.
    - src: Source IP address
    - dst: Destination IP address
    - size: Size of the packet in bytes
    """
    ensure_log_directory()
    logging.warning(f"Anomaly detected: {src} -> {dst}, Size: {size}")