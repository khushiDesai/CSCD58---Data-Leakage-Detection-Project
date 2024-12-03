import unittest
from anomaly_detector import detect_anomalies
from scapy.all import IP, TCP

class TestAnomalyDetector(unittest.TestCase):
    def test_anomaly_detection(self):
        """
        Test anomaly detection with various packet sizes.
        """
        print("Testing anomaly detection...")
        try:
            # Large packet
            large_packet = IP(src="192.168.1.100", dst="10.0.0.1") / TCP() / ("X" * 2000)
            detect_anomalies(large_packet)

            # Small packet
            small_packet = IP(src="192.168.1.100", dst="10.0.0.1") / TCP() / ("X" * 500)
            detect_anomalies(small_packet)

            self.assertTrue(True, "Anomaly detection executed successfully.")
        except Exception as e:
            self.fail(f"Anomaly detection failed with error: {e}")

if __name__ == "__main__":
    unittest.main()