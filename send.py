#!/usr/bin/python2
import socket
import os
import sys
recv_ip = "127.0.0.1"
recv_port = 4444 # 0-1024 are free

#creating udp socket
#              ip type 4,UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# sending data to reciever
while 4 > 2:
	msg = raw_input("Enter your message: ")
	s.sendto(msg,(recv_ip,recv_port))
	if msg=='exit':
		s.close()
		break
	data=s.recvfrom(150)
	if str(data[0]) == 'exit':
		print("exit from other host")
		s.close()
		break
	else:		
		print("Reply from reciever : ", data[0])
	
		
	


