from scapy.all import sniff, IP  # Scapy functions for packet sniffing and IP layer handling
from logger import log_packet  # Function to log captured packets
conf.use_ipv6 = False
def packet_callback(packet, anomaly_callback):
    """
    Callback function to process each captured packet.
    - Logs the packet details if it contains an IP layer.
    - Skips non-IP packets.
    """
    print(f"Captured Packet: {packet.summary()}")

    try:
        # Check if the packet contains an IP layer
        if IP in packet:
            src = packet[IP].src  # Source IP address
            dst = packet[IP].dst  # Destination IP address
            size = len(packet)  # Packet size in bytes
            print(f"Captured Packet: {src} -> {dst}, Size: {size}")
            
            # Log the captured packet
            log_packet(src, dst, size)

            #pass packet to anomaly detection callback
            anomaly_callback(packet)
        else:
            # Skip packets without an IP layer
            print("Non-IP packet captured. Skipping...")
    except Exception as e:
        print(f"Error processing packet: {e}")

def start_sniffing(anomaly_callback):
    """
    Starts packet sniffing using Scapy.
    Captures only IP packets and processes them via packet_callback.
    """
    try:
        sniff(prn=lambda pkt: packet_callback(pkt, anomaly_callback), filter="ip", store=False)  # Sniff IP packets only
    except Exception as e:
        print(f"Error starting packet sniffing: {e}")