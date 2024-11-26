from scapy.all import sniff, IP
from utils.logger import log_packet

def packet_callback(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst
        size = len(packet)
        print(f"Captured Packet: {src} -> {dst}, Size: {size}")
        
        # Log the captured packet
        log_packet(src, dst, size)

def start_sniffing():
    sniff(prn=packet_callback, filter="ip", store=False)