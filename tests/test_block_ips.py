import unittest
from src.block_ips import block_ip, get_blocked_ips
import os
import subprocess

class TestBlockIP(unittest.TestCase):
    def setUp(self):
        """
        Set up initial conditions before each test.
        Clear all iptables rules to ensure a clean slate.
        """
        subprocess.run(["sudo", "iptables", "-F"], check=True)  # Flush all rules

    def tearDown(self):
        """
        Clean up after each test.
        Clear all iptables rules to ensure no leftover configurations.
        """
        subprocess.run(["sudo", "iptables", "-F"], check=True)  # Flush all rules

    def test_block_ip(self):
        """
        Test blocking an IP using iptables.
        """
        test_ip = "192.168.1.100"
        print(f"Blocking IP: {test_ip}")
        try:
            block_ip(test_ip)
            result = subprocess.run(
                ["sudo", "iptables", "-L"], capture_output=True, text=True
            )
            self.assertIn(test_ip, result.stdout, "test_block_ip: IP successfully blocked.")
        except Exception as e:
            self.fail(f"IP blocking failed with error: {e}")
    def test_blocked_multiple_ips(self):
        """
        Test retrieving blocked IPs when some IPs are blocked.
        """
        test_ips = ["192.168.1.100", "10.0.0.5"]
        # Block the test IPs
        for ip in test_ips:
            block_ip(ip)

        # Get the blocked IPs
        blocked_ips = get_blocked_ips()

        # Verify that all test IPs are in the blocked IPs list
        for ip in test_ips:
            self.assertIn(ip, blocked_ips, f"IP {ip} should be in the blocked list.")

    def test_no_blocked_ips(self):
        """
        Test retrieving blocked IPs when no IPs are blocked.
        """
        # Get the blocked IPs
        blocked_ips = get_blocked_ips()

        # Verify that the list is empty
        self.assertEqual(len(blocked_ips), 0, "No IPs should be blocked.")

if __name__ == "__main__":
    unittest.main()