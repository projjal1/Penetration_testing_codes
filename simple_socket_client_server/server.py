#Code for server part on socket

import socket 

#Set the hostname and specify the port
#here the hostname will be the localhost
host = socket.gethostname()
port = 9337

#Connection parameters 
#AF_INET: ipv4 connection
#SOCK_STREAM: TCP/IP connection
sock_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind the connection to the socket and start listening
sock_.bind((host,port))
sock_.listen(1)

print("\nServer started...\n")

#Accept incoming connection on client part
conn,addr = sock_.accept()

print("Connection established with: ",str(addr))

#Send the msg
message = "\nThank you for connecting "+str(addr)
conn.send(message.encode("ascii"))
conn.close()