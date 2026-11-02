# Packet Sniffing using Scapy

from scapy.all import sniff
from scapy.layers.inet import IP

# You must run this as admin sudo python3 examples/scapy_sniffer_example.py
# To run on windows you may need to install Npcap to work with Scapy

# Function to process your packets
def process_packet(packet):
    if IP in packet:
        source = packet[IP].src
        destination = packet[IP].dst
        protocol = packet[IP].proto
        protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
        protocol_name = protocol_map.get(protocol, "Unknown")

        # Live Print
        print(f"[{protocol_name}] Source: {source} Destination: {destination}")

PACKETS_TO_PROCESS = 0  # 0 Here Means Unlimited - Set Your Own or Leave at 0
print("Sniffing Network Packets...\nPress Ctrl+C to stop.\n")

try:
    sniff(count=PACKETS_TO_PROCESS, prn=process_packet, store=False)
except KeyboardInterrupt:
    print("\nStopped Capturing")