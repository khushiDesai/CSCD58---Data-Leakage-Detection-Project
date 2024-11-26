import os

def block_ip(ip):
    """
    Blocks a suspicious IP address using iptables.
    - ip: Source IP address to be blocked.
    """
    os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")  # Adds a rule to block the IP
    print(f"Blocked IP: {ip}")