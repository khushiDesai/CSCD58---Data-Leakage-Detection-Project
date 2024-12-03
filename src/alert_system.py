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
    # Email setup
    sender_email = config['sender_email']
    smtp_server = config['smtp_server']
    smtp_port = config['smtp_port']

    # Compose email
    subject = f"Alert: Suspicious IP Detected - {ip}"
    body = f"Anomaly detected originating from IP:\n\n{ip}\n\nPlease investigate this activity."
    
    # Build the email
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ALERT_EMAIL
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Postfix (local SMTP server)
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.send_message(message)
        print(f"Alert email sent to {ALERT_EMAIL}")
    except Exception as e:
        print(f"Failed to send alert email: {e}")