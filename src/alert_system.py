import json
import smtplib

# Load configuration from thresholds.json
with open('configs/thresholds.json') as f:
    config = json.load(f)

ALERT_EMAIL = config['alert_email']

def send_alert(ip):
    print(f"Sending alert for IP: {ip}")
    # Implement email alert logic here, using ALERT_EMAIL if needed