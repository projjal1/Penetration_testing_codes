#This code is used to discover hidden ssids (wifi network ids)

from scapy.all import *
import os

#Assigning interface of wifi monitor cards
iface = "wlan0"

#Getting the ssid using this function
def h_packet(packet):
    if packet.haslayer(Dot11ProbeReq) or packet.haslayer(Dot11ProbeResp) or packet.haslayer(Dot11AssoReq):
        print "SSID identified " + packet.info

#Starting card in monitor mode
os.system("iwconfig " + iface + "mode monitor")

#Starting the process to sniff
print "Sniffing traffic on interface " + iface
sniff(iface=iface, prn=h_packet)