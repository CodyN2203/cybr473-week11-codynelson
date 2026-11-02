# PCAP Processing with Scapy

#Import some needed libraries
import sys
import os
import socket
from datetime import datetime, timezone

# Scapy Imports Start Here
from scapy.utils import rdpcap  # rdpcap loads packets from a .pcap file so we can read them

from scapy.layers.l2 import Ether, ARP
# Ether reads Ethernet frames so we can see MAC addresses and what type of traffic it is
# ARP reads ARP packets, which are used by devices to learn each other's MAC addresses on the network

from scapy.layers.inet import IP, TCP, UDP, ICMP
# IP reads IPv4 packet information such as source IP, destination IP, and TTL
# TCP reads TCP packets so we can see source and destination ports and flags like SYN or ACK
# UDP reads UDP packets which are similar to TCP but simpler and faster, often used for streaming or DNS
# ICMP reads ping and network diagnostic messages

from scapy.layers.inet6 import IPv6
# IPv6 reads IPv6 packets, which are just the newer version of IP traffic

# I'm going to process only one package to make it easy to break it down in my output
# This code will process all packets if this is set to 0
PACKAGES_TO_PROCESS = 1

# A dictionary map with common IP protocol numbers to names we can read
# We used this in the sniffer example in assignment #10
# Here we set it as a global constant
IP_PROTOCOL_MAP = {
    1: "ICMP",
    6: "TCP",
    17: "UDP",
}

# Common EtherType values
# You can add more if you need more, otherwise the script below will show you the Hex String

ETHER_TYPES = {
    0x0800: "IPv4",
    0x0806: "ARP",
    0x86DD: "IPv6"
}


# Helper Functions

# This gets the port service name - like http | https | stmp (email) | etc.
def port_service_name(port, protocol):
    if port < 0 or port > 65535:
        raise ValueError("Invalid Port")
    try:
        return socket.getservbyport(port, protocol.lower())
    except Exception:
        return "ephemeral" # Temporary Port Essentially

# Function to cleanly format the timestamps from Scapy
def format_timestamp(timestamp):
    try:
        ts_float = float(timestamp)
        return datetime.fromtimestamp(ts_float, tz=timezone.utc).isoformat()
    except Exception as e:
        return f"unknown-time (ts={timestamp!r}, err={e})"

# Main Process
def process_pcap(path):
    print("Scapy PCAP Processor Starting is Parsing:", path)
    try:
        packets = rdpcap(path) # Start Reading Packets at the path
    except FileNotFoundError:
        print("ERROR: File not found.")
        return # Stop Script
    except Exception as e:
        print(f"ERROR: Could not parse PCAP: {e}")
        return # Stop Script

    packages_processed = 0

    if PACKAGES_TO_PROCESS > 0:
        if PACKAGES_TO_PROCESS == 1:
            print(f"\nProcessing a Max of {PACKAGES_TO_PROCESS} Packet.")
        else:
            print(f"\nProcessing a Max of {PACKAGES_TO_PROCESS} Packets.")

    for index, packet in enumerate(packets, start=1):
        # Stop once we hit the limit (0 means process everything)
        if PACKAGES_TO_PROCESS != 0:
            if packages_processed >= PACKAGES_TO_PROCESS:
                break

        packages_processed += 1

        print(packet.summary())  # One line overview of the layers in this packet
        # Scapy Packet has .time (epoch seconds)
        ts = getattr(packet, "time", None)
        ts_str = format_timestamp(ts) if ts is not None else "unknown-time"

        # Consider that a Package is Set Up Like This:
        # [ Shipping Box ]  -> Ethernet (MAC to MAC delivery)
        #    [ Package ]    -> IP (IP to IP delivery)
        #       [ Letter ]  -> TCP/UDP (port to port delivery)
        #          [ Text ] -> Actual data

        # Ethernet (Our Shipping Box) Check if we have it
        if Ether in packet:
            eth = packet[Ether]
            src_mac = eth.src
            dst_mac = eth.dst
            eth_type = eth.type  # hex string EtherType (e.g., 0x0800, 0x0806, 0x86DD)
            frame_type = ETHER_TYPES.get(eth_type, f"0x{eth_type:04x}")

            print("\n" + "=" * 60)
            print(f"Packet #{index}  TIMESTAMP: {ts_str}")
            print("====== ETHERNET LAYER =====")
            print(f"SRC MAC:   {src_mac}")
            print(f"DST MAC:   {dst_mac}")
            print(f"ETHERTYPE: {frame_type}")

        else:
            # Non-Ethernet (Very Rare/Unlikely in typical PCAP files)
            print("\n" + "=" * 60)
            print(f"PKT #{index}  TIMESTAMP: {ts_str}")
            print("No Ethernet layer found; skipping.")
            continue # We stop the package processing here because without this layer there's nothing more to process

        # IPv4
        # Our Package Essentially based on the diagram above after checking ethernet we process IP
        if IP in packet:
            ip = packet[IP]
            src_ip = ip.src
            dst_ip = ip.dst
            ttl = ip.ttl # Time to Live
            # TTL (Time To Live) is a counter that decreases at each router to prevent packets from looping forever
            proto_num = ip.proto
            transport = IP_PROTOCOL_MAP.get(proto_num, str(proto_num))

            print("====== IPv4 LAYER =====")
            print(f"TTL:       {ttl}")
            print(f"SRC IP:    {src_ip}")
            print(f"DST IP:    {dst_ip}")
            print(f"Protocol:  {transport}")

            # TCP
            if TCP in packet:
                tcp_seg = packet[TCP]
                sport, dport = tcp_seg.sport, tcp_seg.dport
                sname = port_service_name(sport, "tcp")
                dname = port_service_name(dport, "tcp")
                flags = tcp_seg.flags
                # TCP flags: S=SYN (start connection), A=ACK (acknowledge), F=FIN (finish), R=RST (reset).
                # Examples: "S"=SYN, "SA"=SYN+ACK, "FA"=FIN+ACK etc. See Scapy Docs for more

                print("------ TCP ------")
                print(f"{src_ip}:{sport} ({sname})  -->  {dst_ip}:{dport} ({dname})")
                print(f"Flags: {flags}")

            # ----- UDP -----
            elif UDP in packet:
                udp_seg = packet[UDP]
                sport, dport = udp_seg.sport, udp_seg.dport
                sname = port_service_name(sport, "udp")
                dname = port_service_name(dport, "udp")

                print("------ UDP ------")
                print(f"{src_ip}:{sport} ({sname})  -->  {dst_ip}:{dport} ({dname})")
                # Length is available as len(udp_seg.payload) + header, but Scapy does not always fill UDP.len
                try:
                    ulen = udp_seg.len
                except Exception:
                    ulen = "unknown"
                print(f"Length: {ulen}")

            # ----- ICMP -----
            elif ICMP in packet:
                ic = packet[ICMP]
                print("------ ICMP ------")
                print(f"Type: {ic.type}  Code: {ic.code}")

        # ARP
        # ARP (Address Resolution Protocol) maps IP addresses to MAC addresses on a local network.
        # It asks "Who has this IP?" so Ethernet knows where to deliver the frame.
        elif ARP in packet:
            arp = packet[ARP]

            # op: 1 = who-has (request), 2 = is-at (reply)

            op_str = "request (who-has)" if arp.op == 1 else "reply (is-at)" if arp.op == 2 else f"op={arp.op}"

            print("====== ARP LAYER =====")
            print(f"Operation: {op_str}")
            print(f"Sender MAC: {arp.hwsrc}   Sender IP: {arp.psrc}")
            print(f"Target MAC: {arp.hwdst}   Target IP: {arp.pdst}")

        # IPv6
        elif IPv6 in packet:
            v6 = packet[IPv6]
            print("====== IPv6 LAYER =====")
            print(f"SRC IP:    {v6.src}")
            print(f"DST IP:    {v6.dst}")

        # You could add more detailed IPv6/transport parsing if needed.
        else:
            print("No IPv4/ARP/IPv6 layer recognized for this Ethernet frame.")


    if packages_processed == 0:
        print("\nNo packets were processed.")
    elif packages_processed == 1:
        print(f"\nA total of {packages_processed} PCAP packet was processed.")
    else:
        print(f"\nA total of {packages_processed} PCAP packets were processed.")

    print("\nScript End.")


target = input("Target PCAP File: ").strip()

if not os.path.isfile(target):
    print("ERROR: Invalid file path.")
    sys.exit(1)

process_pcap(target)
