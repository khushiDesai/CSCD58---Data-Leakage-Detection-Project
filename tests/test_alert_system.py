import unittest
from ../alert_system import send_alert

class TestAlertSystem(unittest.TestCase):
    def test_send_alert(self):
        """
        Test sending email alerts.
        """
        print("Testing email alert...")
        try:
            send_alert("192.168.1.100")  # Test with a dummy IP
            self.assertTrue(True, "Alert function executed successfully.")
        except Exception as e:
            self.fail(f"Alert function failed with error: {e}")

if __name__ == "__main__":
    unittest.main()