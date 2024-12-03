from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from scapy.all import IP, UDP, TCP, ICMP, Raw, send
import time

def generate_unexpected_packets(src_ip, dst_ip):
    """
    Generate unexpected or malicious packets to simulate data leakage or attacks.
    - src_ip: Source IP address for the packets.
    - dst_ip: Destination IP address for the packets.
    """
    print("DEBUG: Setting up the Mininet network...")
    net = Mininet(controller=Controller, link=TCLink)

    try:
        # Add components
        h1 = net.addHost('h1', inNamespace=False)  # Use host networking
        h2 = net.addHost('h2')
        s1 = net.addSwitch('s1')
        c0 = net.addController('c0')

        net.addLink(h1, s1)
        net.addLink(h2, s1)

        # Start the network
        net.start()
        print("DEBUG: Mininet network started with host networking for h1.")

        # Configure DNS for h2
        print("DEBUG: Configuring DNS for h2...")
        h2.cmd("echo 'nameserver 8.8.8.8' > /etc/resolv.conf")
        h2.cmd("echo 'nameserver 8.8.4.4' >> /etc/resolv.conf")
        print("DEBUG: DNS configuration applied to h2.")

        # Test DNS and SMTP reachability from h1
        print("DEBUG: Verifying DNS and SMTP connectivity from h1...")
        dns_test = h1.cmd("ping -c 3 smtp.gmail.com")
        print(f"DEBUG: DNS Test Output:\n{dns_test}")
        smtp_test = h1.cmd("telnet smtp.gmail.com 587")
        print(f"DEBUG: SMTP Test Output:\n{smtp_test}")

        # Deploy detection tool on h1
        print("DEBUG: Starting detection tool on h1...")
        h1.cmd('python3 ../src/main.py &')
        time.sleep(5)  # Wait for the tool to initialize
        print("DEBUG: Detection tool initialized on h1.")

        # Simulate traffic from h2
        print("DEBUG: Simulating traffic from h2 to h1...")
        generate_unexpected_packets(src_ip=h2.IP(), dst_ip=h1.IP())

        # Open CLI for manual inspection
        print("DEBUG: Opening Mininet CLI for manual inspection...")
        CLI(net)

    except Exception as e:
        print(f"DEBUG: Error in network setup or execution: {e}")

    finally:
        # Stop the network
        print("DEBUG: Stopping Mininet network...")
        net.stop()
        print("DEBUG: Mininet network stopped.")

if __name__ == '__main__':
    setup_network()