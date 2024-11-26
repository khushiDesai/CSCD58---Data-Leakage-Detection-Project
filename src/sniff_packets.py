from scapy.all import sniff, IP
from utils.logger import log_packet

def packet_callback(packet):
    try:
        # Check if the packet contains an IP layer
        if IP in packet:
            src = packet[IP].src
            dst = packet[IP].dst
            size = len(packet)
            print(f"Captured Packet: {src} -> {dst}, Size: {size}")
            
            # Log the captured packet
            log_packet(src, dst, size)
        else:
            # Skip packets without an IP layer
            print("Non-IP packet captured. Skipping...")
    except Exception as e:
        print(f"Error processing packet: {e}")

def start_sniffing():
    try:
        sniff(prn=packet_callback, filter="ip", store=False)
    except Exception as e:
        print(f"Error starting packet sniffing: {e}")