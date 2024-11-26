import threading
from sniff_packets import start_sniffing
from anomaly_detector import detect_anomalies
from alert_system import start_alerting
from utils.logger import ensure_log_directory

def main():
    ensure_log_directory()
    print("Starting Data Leakage Detection Tool")
    threading.Thread(target=start_sniffing).start()
    threading.Thread(target=detect_anomalies).start()
    threading.Thread(target=start_alerting).start()

if __name__ == "__main__":
    main()
