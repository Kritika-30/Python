#!/usr/bin/python3
# now importing library
import time
import subprocess
import webbrowser
import os

option='''
Press  1  to  start  your  vlc  media player :
Press  2  to  play your fav song in youtube :  
Press  3  to  search something  on google   :  
Press  4  to  send whatsapp message to your fav number  :  
Press  5  to  check current  time and date  :
press  6  to  reboot your machine  : 
'''
print(option)
#Input from user in str format
choice = input()

if option == '1':
	# to connect OS level application subprocess is used
	subprocess.getoutput('vlc')	

elif option == '2':
	data = input("Type your fav song")
	webbrowser.open("https://www.youtube.com/watch?v="+data)

elif option == '3':
	# to know what user wants to search
	data = input("Type your new search:")
	webbrowser.open_new_tab("https://www.google.com/search?q="+data) 

	 

elif option == '5':
	current_time = time.ctime()
	print(current_time)

elif option == '6':
	os.system("reboot")	  
	
    
 

