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
        except FileExistsError:
            # The directory was created by another process
            pass
    else:
        print(f"Log directory file already exists: {log_dir}")

def check_file_exit():
    log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)),"src","logs","system.log")
    if not os.path.exists(log_file):
        try: 
            print(f"Creating log file: {log_file}")
            with open(log_file, "w") as f:
                pass
        except Exception as e:
            raise RuntimeError(f"Error ensuring log file '{log_file}': {e}")

ensure_log_directory()

# Configure logging settings
logging.basicConfig(
    filename="logs/system.log",
    filemode='a', #append file
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
    check_file_exit()
    logging.info(f"Packet: {src} -> {dst}, Size: {size}")

def log_anomaly(src, dst, size):
    """
    Logs details of a detected anomaly.
    - src: Source IP address
    - dst: Destination IP address
    - size: Size of the packet in bytes
    """
    check_file_exit()
    logging.warning(f"Anomaly detected: {src} -> {dst}, Size: {size}")