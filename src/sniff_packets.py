from scapy.all import sniff, IP  # Scapy functions for packet sniffing and IP layer handling
from utils.logger import log_packet  # Function to log captured packets

def packet_callback(packet):
    """
    Callback function to process each captured packet.
    - Logs the packet details if it contains an IP layer.
    - Skips non-IP packets.
    """
    try:
        # Check if the packet contains an IP layer
        if IP in packet:
            src = packet[IP].src  # Source IP address
            dst = packet[IP].dst  # Destination IP address
            size = len(packet)  # Packet size in bytes
            print(f"Captured Packet: {src} -> {dst}, Size: {size}")
            
            # Log the captured packet
            log_packet(src, dst, size)
        else:
            # Skip packets without an IP layer
            print("Non-IP packet captured. Skipping...")
    except Exception as e:
        print(f"Error processing packet: {e}")

def start_sniffing():
    """
    Starts packet sniffing using Scapy.
    Captures only IP packets and processes them via packet_callback.
    """
    try:
        sniff(prn=packet_callback, filter="ip", store=False)  # Sniff IP packets only
    except Exception as e:
        print(f"Error starting packet sniffing: {e}")