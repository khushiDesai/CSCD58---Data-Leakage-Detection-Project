import unittest
from src.block_ips import block_ip
import os

class TestBlockIP(unittest.TestCase):
    def test_block_ip(self):
        """
        Test blocking an IP using iptables.
        """
        test_ip = "192.168.1.100"
        print(f"Blocking IP: {test_ip}")
        try:
            block_ip(test_ip)
            # Check if the IP was added to iptables
            result = os.popen(f"sudo iptables -L | grep {test_ip}").read()
            self.assertIn(test_ip, result, "IP successfully blocked.")
        except Exception as e:
            self.fail(f"IP blocking failed with error: {e}")

if __name__ == "__main__":
    unittest.main()