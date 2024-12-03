import unittest
from src.block_ips import block_ip
import os
import subprocess

class TestBlockIP(unittest.TestCase):
    def test_block_ip(self):
        """
        Test blocking an IP using iptables.
        """
        test_ip = "192.168.1.100"
        print(f"Blocking IP: {test_ip}")
        try:
            result = subprocess.run(
                ["sudo", "iptables", "-L"], capture_output=True, text=True
            )
            self.assertIn(test_ip, result.stdout, "IP successfully blocked.")
        except Exception as e:
            self.fail(f"IP blocking failed with error: {e}")

if __name__ == "__main__":
    unittest.main()