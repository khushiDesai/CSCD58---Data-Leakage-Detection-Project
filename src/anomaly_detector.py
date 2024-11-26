import json
from alert_system import send_alert
from block_ips import block_ip
from utils.logger import log_anomaly

# Load configuration from thresholds.json
with open('configs/thresholds.json') as f:
    config = json.load(f)

THRESHOLD_SIZE = config['threshold_size']

def detect_anomalies(packet):
    try:
        # Ensure the packet has an IP layer
        if IP in packet:
            src = packet[IP].src
            dst = packet[IP].dst
            size = len(packet)

            # Check for anomalies
            if size > THRESHOLD_SIZE:
                print(f"Anomaly detected: Large packet from {src} -> {dst}, Size: {size}")
                
                # Log the detected anomaly
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