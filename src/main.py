import threading
from sniff_packets import start_sniffing
from anomaly_detector import detect_anomalies
from alert_system import start_alerting
from utils.logger import ensure_log_directory

def main():
    """
    Main function to initialize the Data Leakage Detection Tool.
    - Ensures the log directory exists.
    - Starts separate threads for packet sniffing, anomaly detection, and alert handling.
    """
    ensure_log_directory()
    print("Starting Data Leakage Detection Tool")
    threading.Thread(target=start_sniffing).start()  # Start packet sniffing in a separate thread
    threading.Thread(target=detect_anomalies).start()  # Start anomaly detection in a separate thread
    threading.Thread(target=start_alerting).start()  # Start the alert system in a separate thread

if __name__ == "__main__":
    main()
