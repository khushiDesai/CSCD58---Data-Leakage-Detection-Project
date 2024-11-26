import json
from alert_system import send_alert
from block_ips import block_ip
from utils.logger import log_anomaly

# Load configuration from thresholds.json
with open('configs/thresholds.json') as f:
    config = json.load(f)

THRESHOLD_SIZE = config['threshold_size']

def detect_anomalies(packet):
    if len(packet) > THRESHOLD_SIZE:
        src = packet[IP].src
        dst = packet[IP].dst
        size = len(packet)
        print(f"Anomaly detected: Large packet from {src} -> {dst}, Size: {size}")
         # Log the detected anomaly
        log_anomaly(src, dst, size)
        if "send_alert" in config["response_actions"]:
            send_alert(packet[IP].src)
        if "block_ip" in config["response_actions"]:
            block_ip(packet[IP].src)