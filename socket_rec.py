#!/usr/bin/python3
#receiver's code
import socket

#target machine's ip number
target_ip = "0.0.0.0"

#target machine's port number

target_port = 8888

#create UDP socket
#                 IPv4--(INET--INET6), type of socket UDP --(DGRAM--STREAM)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((target_ip,target_port))

while True:
    mydata = s.recvfrom(100) #100 is the maximum size of message
    print(mydata)
    s.sendto("Nice".encode('ascii'),mydata[1])
