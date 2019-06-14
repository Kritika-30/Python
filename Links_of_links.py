#!/usr/bin/python

import webbrowser
from googlesearch import search

#to take input of search
web=input('Enter what to search')
url=[]

#Now to search

for each_search in search(web,stop=5):
	url.append(each_search)
	print(each_search)              #print each searched link
	webbrowser.open_new_tab(each_search)
	for each in search(each_search,stop=5):    #to search again in above 5 links
		print(each)             #print each searched link
		webbrowser.open_new_tab(each)	

	
