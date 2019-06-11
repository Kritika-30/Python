#!/usr/bin/python

import os
import crypt
username = input('Enter a username ')

#checking all the characters are string or not
name=username.isalpha()

if name:
   password = "hello"+username
   encryptpwd = crypt.crypt(password,"22")  
   os.system("useradd -p "+encryptpwd+" "+username)
   print('User has been created')

else :
    print('User cannot be created')   

