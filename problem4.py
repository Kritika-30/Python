#!/usr/bin/python

import os
import crypt
username = input('Enter a username ')

#checking all the characters are string or not
name=username.isalpha()

if name:
   print('User has been created')
   password = 'hello'+ username
   encryptpwd = crypt.crypt(password,'*')  
   os.system('useradd -p'+ str(encryptpwd)+' '+ username)
   

else :
    print('User cannot be created')   

