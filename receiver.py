#!/usr/bin/python3
import socket

rec_port=11005
rec_ip="127.0.0.1"
					#address family  ipv4  and UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((rec_ip,rec_port))
while True:
	print("sender message=",s.recv(100).decode('utf-8'))
	#response=input("send response=")
	#s.sendto(response.encode('utf-8'),(rec_ip,rec_port))
