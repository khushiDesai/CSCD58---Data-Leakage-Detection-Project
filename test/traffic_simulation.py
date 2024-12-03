from scapy.all import send, IP, TCP

# Simulate malicious large packets
packet = IP(dst="10.0.0.1") / TCP() / ("X" * 2000)  # Adjust size
send(packet, count=10)
