import logging
import os

def ensure_log_directory():
    """
    Ensures the 'logs' directory exists. Creates it if it doesn't.
    """
    if not os.path.exists('logs'):
        os.makedirs('logs')

ensure_log_directory()

# Configure logging settings
logging.basicConfig(
    filename="logs/system.log",
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
    logging.info(f"Packet: {src} -> {dst}, Size: {size}")

def log_anomaly(src, dst, size):
    """
    Logs details of a detected anomaly.
    - src: Source IP address
    - dst: Destination IP address
    - size: Size of the packet in bytes
    """
    logging.warning(f"Anomaly detected: {src} -> {dst}, Size: {size}")