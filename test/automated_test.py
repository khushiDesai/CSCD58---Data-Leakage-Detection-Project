from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from scapy.all import IP, UDP, TCP, ICMP, Raw, send
conf.use_ipv6 = False

def generate_unexpected_packets(src_ip, dst_ip):
    """
    Generate unexpected or malicious packets to simulate data leakage or attacks.
    - src_ip: Source IP address for the packets.
    - dst_ip: Destination IP address for the packets.
    """
    print("Generating unexpected packets...")

    # 1. Large Packets
    large_packet = IP(src=src_ip, dst=dst_ip) / Raw(load="X" * 2000)  # Payload > 1500 bytes
    send(large_packet, count=5)  # Send 5 large packets

    # 2. Malformed Packet
    malformed_packet = IP(src=src_ip) / Raw(load="Malformed")
    send(malformed_packet, count=3)  # Send 3 malformed packets

    # 3. Unauthorized Protocol (UDP)
    unauthorized_packet = IP(src=src_ip, dst=dst_ip) / UDP(dport=1234) / Raw(load="Unexpected UDP")
    send(unauthorized_packet, count=4)  # Send 4 UDP packets

    # 4. Spoofed Packets
    spoofed_packet = IP(src="192.168.99.99", dst=dst_ip) / TCP(dport=80) / Raw(load="Spoofed Data")
    send(spoofed_packet, count=2)  # Send 2 spoofed packets

    print("Unexpected packets sent.")

def setup_network():
    # Initialize Mininet
    net = Mininet(controller=Controller, link=TCLink)

    # Add components
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    s1 = net.addSwitch('s1')
    c0 = net.addController('c0')

    net.addLink(h1, s1)
    net.addLink(h2, s1)

    # Start the network
    net.start()

        # Disable IPv6 on all hosts
    for host in [h1, h2]:
        host.cmd('sysctl -w net.ipv6.conf.all.disable_ipv6=1')
        host.cmd('sysctl -w net.ipv6.conf.default.disable_ipv6=1')
    # Deploy detection tool
    h1.cmd('python3 ../src/main.py &')  # Start tool on h1

    # Simulate traffic
    traffic_output = h2.cmd('python3 traffic_simulation.py')
    print("Traffic Output:", traffic_output)

    # Open CLI for further inspection
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == '__main__':
    setup_network()
