#!/usr/bin/python3
import socket


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
	msg=input("enter the message=")
	s.sendto(msg.encode('utf-8'),('127.0.0.1',11005))
	#print("receiver message=",s.recv(100).decode('utf-8'))
