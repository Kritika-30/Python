#!/usr/bin/python

from datetime import date

name=input('Enter your name: ')
age=int(input('Enter your age as on 31 Dec of current year: '))

Year = (date.today()).year - age + 95 

print('You will turn 95 in:')
print(Year)


