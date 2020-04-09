#This code is used for banner grabbing and hostname finding

import sys 
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + "<url>")
    sys.exit(1)

#part for grabbing the banner
req = requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))

#part for obtaining the hostname
gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of "+sys.argv[1]+" is: "+gethostby_ + "\n")
