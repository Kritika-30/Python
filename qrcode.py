#!/usr/bin/python
from googlesearch import search
import os
import pyqrcode

# input fron user to search
web=input("Enter what to search")
num=0
for each_search in search(web,tld='com',lang='en',num=3,start=0,stop=3,pause=1):
	# create qrcode for the search 
	q=pyqrcode.create(each_search)
	print(each_search)
	#create a png file 
	q.png("qr{}.png".format(num),scale=8)
	#to transfer the qrcode at /var/www/html
	os.system("scp -i /home/kritika/Desktop/linuxredhat.pem qr"+str(num)+".png ec2-user@<ip>:/var/www/html/") # add your ip address at <ip>
	num = num+1
