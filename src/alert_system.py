import json
import smtplib

# Load configuration settings from thresholds.json
with open('configs/thresholds.json') as f:
    config = json.load(f)

ALERT_EMAIL = config['alert_email']  # Email address to which alerts will be sent

def send_alert(ip):
    """
    Sends an email alert when a suspicious IP is detected.
    - ip: Source IP address flagged as suspicious.
    """
    print(f"Sending alert for IP: {ip}")