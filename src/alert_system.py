import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Resolve the absolute path to the `configs/thresholds.json` file
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'configs/thresholds.json')

# Load configuration settings from thresholds.json
with open(CONFIG_PATH) as f:
    config = json.load(f)


ALERT_EMAIL = config['alert_email']  # Email address to which alerts will be sent

def send_alert(ip):
    """
    Sends an email alert to all configured recipients when a suspicious IP is detected.
    - ip: Source IP address flagged as suspicious.
    """
    print(f"DEBUG: Preparing to send alert for IP: {ip}")
    
    # Load configuration settings
    sender_email = config.get('sender_email')
    smtp_server = config.get('smtp_server')
    smtp_port = config.get('smtp_port')
    recipients = config.get('alert_email', [])
    sender_password = config.get('sender_password')

    # Compose email
    subject = f"Alert: Suspicious IP Detected and Blocked - {ip}"
    body = (
        f"Anomaly detected originating from IP:\n\n"
        f"{ip}\n\n"
        f"The IP address has been automatically blocked to prevent further activity.\n\n"
        f"Please investigate this activity and take necessary actions."
    )

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ", ".join(recipients)
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        print("DEBUG: Connecting to SMTP server...")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.set_debuglevel(1)  # Enable detailed SMTP debugging
            server.starttls()
            server.login(sender_email, sender_password)
            print("DEBUG: Login successful.")
            server.send_message(message)
        print(f"DEBUG: Alert email successfully sent to {recipients}")
    except Exception as e:
        print(f"DEBUG: Failed to send alert email. Error: {e}")