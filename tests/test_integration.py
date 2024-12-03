import unittest
from scapy.all import IP, TCP
from src.anomaly_detector import detect_anomalies
from src.logger import log_anomaly
from src.block_ips import block_ip

class TestIntegration(unittest.TestCase):
    def test_full_workflow(self):
        """
        Test the full workflow of the data detection tool.
        """
        print("Testing full workflow...")
        packet = IP(src="192.168.1.100", dst="10.0.0.1") / TCP() / ("X" * 2000)

        # Log the packet
        log_anomaly(packet[IP].src, packet[IP].dst, len(packet))

        # Detect anomaly and trigger response actions
        detect_anomalies(packet)

        # Check if the IP was blocked
        blocked_ip = packet[IP].src
        result = os.popen(f"sudo iptables -L | grep {blocked_ip}").read()
        self.assertIn(blocked_ip, result, "Full workflow executed successfully.")

if __name__ == "__main__":
    unittest.main()