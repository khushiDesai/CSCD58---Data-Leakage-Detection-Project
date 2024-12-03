import json
import os
from alert_system import send_alert  # Function to send alerts for suspicious activity
from block_ips import block_ip  # Function to block suspicious IP addresses
from logger import log_anomaly  # Function to log detected anomalies

# Resolve the absolute path to the `configs/thresholds.json` file
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'configs/thresholds.json')

# Load configuration settings from thresholds.json
with open(CONFIG_PATH) as f:
    config = json.load(f)

THRESHOLD_SIZE = config['threshold_size']  # Packet size threshold for anomaly detection

def detect_anomalies(packet):
    """
    Detects suspicious network activity based on packet size and other criteria.
    - packet: Captured network packet.
    """
    try:
        # Ensure the packet contains an IP layer
        if IP in packet:
            src = packet[IP].src  # Source IP address
            dst = packet[IP].dst  # Destination IP address
            size = len(packet)  # Packet size in bytes

            # Check if the packet exceeds the defined size threshold
            if size > THRESHOLD_SIZE:
                print(f"Anomaly detected: Large packet from {src} -> {dst}, Size: {size}")
                
                # Log the anomaly for record-keeping
                log_anomaly(src, dst, size)

                # Execute configured response actions
                if "send_alert" in config["response_actions"]:
                    send_alert(src)
                if "block_ip" in config["response_actions"]:
                    block_ip(src)
        else:
            print("Non-IP packet encountered in anomaly detection. Skipping...")
    except Exception as e:
        print(f"Error in anomaly detection: {e}")