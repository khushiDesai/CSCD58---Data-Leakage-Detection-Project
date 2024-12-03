import os

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