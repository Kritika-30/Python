#!/usr/bin/python

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
list1=[]
list2=[]
# condition 1
print('No. greater than 5')
for each in adhoc:
	if each > 5:
	   print(each)
	   list1.append(each)

# condition 2
print('No. less than or equal to 2')
for each in adhoc:
	if each <= 2:
	   print(each)
	   list2.append(each)

# condition 3
print('list 1:')
print(list1)
print('list 2:') 
print(list2)

