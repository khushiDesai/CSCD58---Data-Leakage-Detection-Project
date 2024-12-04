import threading
from sniff_packets import start_sniffing  # Captures network packets
from anomaly_detector import detect_anomalies  # Detects anomalies in captured packets
from logger import ensure_log_directory  # Ensures logs directory exists

def main():
    """
    Main function to initialize the Data Leakage Detection Tool.
    - Ensures the log directory exists.
    - Starts separate threads for packet sniffing and anomaly detection.
    """
    ensure_log_directory()
    print("Starting Data Leakage Detection Tool")
    threading.Thread(target=start_sniffing, args=(detect_anomalies,)).start()  # Start packet sniffing
    
if __name__ == "__main__":
    main()