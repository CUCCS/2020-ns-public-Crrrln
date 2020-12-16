#! /usr/bin/python

from scapy.all import *

dst_ip = "172.16.111.117"
src_port = RandShort()
dst_port=8083

tcpconnectscan_pkts = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)
#if(str(type(tcpconnectscan_pkts))=="<type 'NoneType'>"):
if tcpconnectscan_pkts is None:
    print("Filtered")
elif(tcpconnectscan_pkts.haslayer(TCP)):
    if(tcpconnectscan_pkts.getlayer(TCP).flags == 0x12):
        #send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=10)
        print("Open")
    elif (tcpconnectscan_pkts.getlayer(TCP).flags == 0x14):
        print("Closed")
