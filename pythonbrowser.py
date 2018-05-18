#!user/bin/python3
import time
import datetime
import webbrowser as w
import nmap
import warnings
# pytz use for time zone
import pytz 
#bs4 is use for webscrapping
from bs4 import BeautifulSoup 
#load The page 
import requests
# use for system platform like window ,linux,mac
from sys import platform
import ipwhois 

option ='''
press 1:to enter any word to split each word and search on google
press 2:to enter any word and show the image of each word on google
press 3:to enter any word and show the url of each word 
press 4: current time and date
press 5: open default webbrowser
press 6: all nework id
press 7: enter the domain name and find owner ,email and contact
'''
print(option)
ch=input()
if ch=='1':
	search_data=input("enter data=")
	final_data=search_data.strip() #remove leading and trailing space
	done_data=final_data.split() #split each word by space
	print(done_data)
	for i in done_data:
		webbrowser.open_new_tab("https://www.google.com/search?q="+i)
		
if ch=='2':
	search_data=input("enter data=")
	final_data=search_data.strip() #remove leading and trailing space
	done_data=final_data.split() #split each word by space
	print(done_data)
	for i in done_data:
		w.open_new_tab('https://www.google.co.in/search?q={}&source=lnms&tbm=isch'.format(i))
if ch=='3':
	search_data=input("enter data=")
	final_data=search_data.strip()
	done_data=final_data.split()
	for i in done_data:
		url= "https://wwws.google.com"+i
		page=requests.get(url).content
		bs=BeautifulSoup(page,'lxml')
		c=bs.find_all('a')
		for  i in c:
			print(i.get('href'))	
		
		
#for datetime and time zone
if ch=='4':
	now=datetime.datetime.now(pytz.utc)
	print(now)

#for platform show wich os we are using
if ch=='5':
	platform=input("enter your platform=")
	if platform=="linux":
		w.get('firefox').open_new_tab("https://www.google.com")
	elif platform=="win32":
		w.get('InternetExplore').open_new_tab("https://www/google.com")
	elif platform=="darwin":
		w.get('safari').open_new_tab("https://www.google.com")	

if ch=='6':
	n=nmap.PortScanner()
	p1=n.scan('192.168.43.138 ','22-443')
	p=n.all_hosts()
	#print(p1)
	print(p)

if ch=='7':
	detail=ipwhois.IPWhois('172.217.160.238')
	with warnings.catch_warnings():
			warnings.filterwarnings("ignore",category=UserWarning)
			d=detail.lookup_whois()
			print(d['nets'])

