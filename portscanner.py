import sys
import socket 
import nmap 

if len(sys.argv)<2:
    print("Usage is : "+sys.argv[0]+"<ip>")
    exit(1)

#target url
url=sys.argv[1]

#target_ip
target=socket.gethostbyname(url)
target=str(target)
print("Target ip of host is "+target)

#Custom list of ports 
ports=[21,22,53,80,110,139,443,8080]

#nmap variable
var=nmap.PortScanner()

#Checks for open/close of port state
for each in ports:
    resp=var.scan(target,str(each))
    print('Port ',each,' is ',resp['scan'][target]['tcp'][each]['state'])

#Server is live/down
print("Host is ",resp['scan'][target]['status']['state'])