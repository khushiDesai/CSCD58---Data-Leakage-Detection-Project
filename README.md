# **CSCD58---Data-Leakage-Detection-Tool-Project**

## **Description and Explanation of the Project**

The **Data Leakage Detection Tool** is a simplified yet practical system designed to detect potential data leakage within a network. The project focuses on real-time monitoring, anomaly detection, and automated response to mitigate risks. Leveraging tools like Mininet for network simulation, Wireshark for traffic analysis, and Scapy for packet handling, this tool provides foundational support for network security.


### **Project Goals**
1. **Real-time Network Traffic Monitoring**:
   - Capture and inspect network traffic using tools like Mininet and Wireshark.
   - Monitor key attributes such as packet size, destination IP, and access patterns to establish a baseline for normal behavior.
   
2. **Anomaly Detection**:
   - Implement signature-based and statistical methods for detecting abnormal behaviors, such as large data transfers or unknown IP addresses.
   - Explore machine learning techniques like clustering or isolation forests for advanced anomaly detection (if time permits).

3. **Alert and Response Mechanism**:
   - Develop a notification system with categorized threat severity levels.
   - Automate responses like IP blacklisting to minimize potential damage.

4. **Testing and Evaluation**:
   - Simulate data leakage scenarios in controlled environments using Mininet.
   - Measure performance with metrics like false positives/negatives.

5. **Documentation and Presentation**:
   - Produce a detailed report covering all phases of the project.
   - Create a video demonstration showcasing the tool’s functionality.

---

## **Team Contributions**

### **Khushi Desai** (1006326192)
- Designed and implemented the **anomaly detection logic**.
- Integrated **logging systems** to track and record network anomalies.
- Developed the **real-time network monitoring scripts** using Scapy and Wireshark.
- Contributed to the **testing phase** by simulating data leakage scenarios in Mininet.
- Authored sections of the documentation, including implementation details and analysis.

### **Vicky Chen** (1007121838)
- Configured the **alert system** to send notifications for detected anomalies.
- Designed and implemented the **automated IP blocking mechanism** using `iptables`.
- Assisted in testing and analyzing false positives/negatives from anomaly detection.
- Developed and presented the video demonstration of the tool.
- Contributed to the **report writing**, focusing on goals, results, and concluding remarks.

---

## **Instructions to Run and Test the Tool**

### **Prerequisites**
- **System Requirements**: Ubuntu-based system or VM (e.g., Mininet VM).
- **Dependencies**:
  - Python 3.8+
  - Scapy
  - Mininet
  - Wireshark (optional)
  - Postfix (for email alerts)

### **Install dependencies**:
```bash
sudo apt update
sudo apt install python3-pip mininet postfix iptables
pip3 install scapy
```

### **Steps to Run**:
1. **Clone the Repository**:
    git clone https://github.com/khushiDesai/CSCD58---Data-Leakage-Detection-Project.git
    cd CSCD58---Data-Leakage-Detection-Project

2. **Start the Tool**: Launch the tool on a Mininet host:
    sudo python3 src/main.py

3. **Simulate Traffic**: Use the provided traffic_simulation.py script to generate normal and anomalous traffic:
    python3 tests/traffic_simulation.py <destination_ip>

4. **Check Logs**: View logged anomalies:
    cat logs/system.log

5. **Test Components Individually**: Run tests for specific modules:
    python3 -m unittest tests/test_alert_system.py
    python3 -m unittest discover -s tests -p "*.py"

---

## **Implementation Details and Documentation**

### **Core Features**
- Packet Sniffing:
    - Real-time packet capture using Scapy with IP filtering.
- Anomaly Detection:
    - Detect anomalies based on packet size thresholds and patterns.
    - Modular configuration using thresholds.json.
- Logging:
    - Captures details of each packet and anomaly in logs/system.log.
- Alert System:
    - Sends email notifications for detected anomalies using Postfix.
- Automated Response:
    - Dynamically blocks suspicious IPs using iptables.

---

## **File Structure**
```
CSCD58---Data-Leakage-Detection-Project
│   README.md 
│
└───src
│   └───configs/
│   │   │   thresholds.json # Configuration thresholds
│   │   alert_system.py # Email alert functionality
│   │   anomaly_dectector.py # Anomaly detection logic
│   │   block_ips.py    # IP blocking functionality
│   │   logger.py  # Logging system
│   │   main.py # Main script to run the tool
│   │   sinff_packets.py    # Packet sniffing logic
│   
└───tests
│   └───logs/
│   │   │   system.log # Log file for captured packets and anomalies
│   │   test_alert_system.py    # Test for alert system
│   │   test_anomaly_dectector.py   # Test for anomaly dectection
│   │   test_block_ips.py   # Test for IP blocking
│   │   test_logger.py  # Test for logging
│   │   traffic_simulation.py   # Traffic generation script
│   │   automated_test.py   # Automated testing scripts

```

## **Analysis and Discussion**
- Results
    - Successfully detected anomalies based on predefined thresholds.
    - IP blocking and alerting mechanisms worked as intended, mitigating potential risks.
    - Simulated scenarios in Mininet demonstrated realistic behaviors, validating the tool’s utility.
- Performance Metrics
    - Accuracy: Low false positives/negatives under tested scenarios.
    - Efficiency: Real-time detection with minimal latency.
- Challenges
    - Ensuring compatibility across different network environments.
    - Managing the balance between detection sensitivity and false positives.

---

## **Concluding Remarks**
The Data Leakage Detection Tool achieved its goal of providing a simplified yet effective network monitoring solution. While basic in its design, the tool lays the foundation for more advanced implementations incorporating machine learning and dynamic threat modeling.

### **Lessons Learned**
1. Importance of Modular Design:
    - Breaking the project into clear, testable components simplifies debugging and collaboration.
2. Real-World Challenges:
    - Network environments can vary greatly, emphasizing the need for adaptable configurations.
3. Teamwork:
    - Collaboration and division of tasks significantly enhanced project efficiency.

Future work could focus on incorporating machine learning for adaptive anomaly detection and improving scalability for larger networks.
