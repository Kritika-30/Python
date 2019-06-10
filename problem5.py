#!/usr/bin/python

import datetime as dt
name=input('Enter your name')
now = dt.datetime.now().hour
if now > 0 and now < 12:
   print('Good Morning',name)
elif now >= 12 and now < 17:
   print('Good Afternoon',name)
elif now >= 17 and now < 21:
   print('Good Evening',name)
elif now <= 21 and now > 24:
   print('Good Night',name)

