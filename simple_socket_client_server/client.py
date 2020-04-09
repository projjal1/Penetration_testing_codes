#Code for client part on socket

import socket

#Connection parameters 
#AF_INET: ipv4 connection
#SOCK_STREAM: TCP/IP connection
sock_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#fetching the hostname of all listeners on port 9337 
sock_.connect((socket.gethostname(),9337))

#receive the message from the server and 1024 bytes
msg = sock_.recv(1024)
sock_.close()

#printing the decoded message
print(msg.decode("ascii"))