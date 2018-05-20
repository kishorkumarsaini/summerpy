#!/usr/bin/python2
import socket
import matplotlib.pyplot as plt

rev_ip='127.0.0.1'
rev_port=10001
#iv4 family  and UDP==============
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((rev_ip,rev_port))
arr=[]
while 4>2:
	clinet=s.recv(1000).decode('utf-8')
	print("sender message=",clinet)
	p=clinet.strip().split()
	print(p)
	d=set(p)
	dic={}
	for i in d:
		dic[i]=p.count(i)
		print("&&&&&&&&&&&&&&&&&&&&")
		print(dic)
		arr=list(dic.values())
		print("*************************")
		print(arr)
	x=arr[0]
	y=arr[1]
	x1=arr[2]
	y1=arr[3]
	print(x)
	print(y)
	print(x1)
	print(y1)


	plt.scatter(x,y,linewidth="5",label="safe",marker="*" ,color='g')
	plt.scatter(x1,y1,linewidth="5",label="danger",marker="+" ,color='g')
	#x=None
	#y=None
	plt.title("This is data visualization")
	plt.xlabel("Distance")
	plt.ylabel("Time")
	plt.legend()
	plt.grid(True, color='k')
	plt.show()