from scapy.all import send, IP, TCP
conf.use_ipv6 = False

# Simulate malicious large packets
packet = IP(dst="10.0.0.1") / TCP() / ("X" * 1500)  # Adjust size
send(packet, count=10)
