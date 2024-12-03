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
    print(f"Sending alert for IP: {ip}")
    sender_email = config['sender_email']
    smtp_server = config['smtp_server']
    smtp_port = config['smtp_port']
    recipients = config['alert_email']  # List of alert emails

    # Compose email
    subject = f"Alert: Suspicious IP Detected and Blocked - {ip}"
    body = (
        f"Anomaly detected originating from IP:\n\n"
        f"{ip}\n\n"
        f"The IP address has been automatically blocked to prevent further activity.\n\n"
        f"Please investigate this activity and take necessary actions."
    )

    # Build the email
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ", ".join(recipients)  # Join multiple emails with commas
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, config['sender_password'])  # Authenticate
            server.send_message(message)
        print(f"Alert email sent to {recipients}")
    except Exception as e:
        print(f"Failed to send alert email: {e}")