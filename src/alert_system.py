import json
import os
import smtplib

# Resolve the absolute path to the `configs/thresholds.json` file
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'configs/thresholds.json')

# Load configuration settings from thresholds.json
with open(CONFIG_PATH) as f:
    config = json.load(f)


ALERT_EMAIL = config['alert_email']  # Email address to which alerts will be sent

def send_alert(ip):
    """
    Sends an email alert when a suspicious IP is detected.
    - ip: Source IP address flagged as suspicious.
    """
    print(f"Sending alert for IP: {ip}")