import logging
import os

def ensure_log_directory():
    if not os.path.exists('logs'):
        os.makedirs('logs')

# Configure logging
logging.basicConfig(filename="logs/system.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_packet(src, dst, size):
    logging.info(f"Packet: {src} -> {dst}, Size: {size}")

def log_anomaly(src, dst, size):
    logging.warning(f"Anomaly detected: {src} -> {dst}, Size: {size}")