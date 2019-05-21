#!/usr/bin/python3

import socket

#target machine's ip number
target_ip = '3.82.4.173'

#target machine's port number

target_port = 8888

#create UDP socket
#                 IPv4--(INET--INET6), type of socket UDP --(DGRAM--STREAM)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Please enter your message : ")
    n = msg.encode('ascii')
    s.sendto(n, (target_ip,target_port))
    print(s.recvfrom(100))
