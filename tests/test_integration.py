import os
import sys
import unittest
from scapy.all import IP, TCP
from src.anomaly_detector import detect_anomalies
from src.logger import log_anomaly
from src.block_ips import block_ip
import subprocess

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
        try:
            result = subprocess.run(
                "sudo iptables -L | grep 192.168.1.100",
                shell=True,  # Use shell to interpret the pipe
                capture_output=True,
                text=True,
                check=True,
            )
            self.assertIn(blocked_ip, result.stdout, "Full workflow executed successfully.")
        except subprocess.CalledProcessError as e:
            self.fail(f"Error checking blocked IP: {e}")

if __name__ == "__main__":
    unittest.main()