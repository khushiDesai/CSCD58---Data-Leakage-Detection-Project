import os
import subprocess

def block_ip(ip):
    """
    Blocks a suspicious IP address using iptables.
    - ip: Source IP address to be blocked.
    """
    try:
        result = subprocess.run(
            ["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"],
            capture_output=True,
            text=True
        )

        #Check for errors
        if result.returncode == 0:
            print(f"Blocked IP: {ip}")
        else:
            print(f"Failed to block IP {ip}: {result.stderr}")
    except Exception as e:
        print(f"Error blocking IP {ip}: {e}")

def get_blocked_ips():
    """
    Retrieves all IPs currently blocked by iptables.
    Returns:
        A list of blocked IP addresses.
    """
    try:
        # Run the iptables command to list rules
        result = subprocess.run(
            ["sudo", "iptables", "-L", "INPUT", "-v", "-n"],
            capture_output=True,
            text=True
        )

        # Check for errors
        if result.returncode != 0:
            print(f"Failed to retrieve iptables rules: {result.stderr}")
            return []

        # Parse the output to find blocked IPs
        blocked_ips = []
        for line in result.stdout.splitlines():
            if "DROP" in line:  # Look for DROP rules
                parts = line.split()
                if len(parts) >= 7:  # Ensure the line contains enough columns
                    ip = parts[4]  # IP is in the 4th column
                    blocked_ips.append(ip)
        return blocked_ips

    except Exception as e:
        print(f"Error retrieving blocked IPs: {e}")
        return []
