#!/usr/bin/python3

import sys
import os

option=(sys.argv[1])  # to take options of cat command from user
filename=(sys.argv[2:])  # to take filename from user

# -n : option to no. all output lines
if option=='-n':
    no_of_line=1
    for each_name in filename :
        try:
            f = open(each_name,'r')
            for i in f:
                print(str(no_of_line)+' '+i, end="")
                no_of_line +=1
            f.close()
        except Exception as e:
            print(e)

# -b : option to number non-empty output lines            
elif option=='-b':
    no_of_line=1
    for each_name in filename :
        try:
            f = open(each_name,'r')
            for i in f:
                if i == '\n' :
                    print(i.rstrip())
                    no_of_line += 0
                else :
                    print(str(no_of_line)+' '+i.rstrip())
                    no_of_line += 1
            f.close()
        except Exception as e:
            print(e)

# -E : option to display $ at the end of each line 
elif option=='-E':
    no_of_line=1
    for each_name in filename :
        try:
            f = open(each_name,'r')
            for i in f:
                print(i.rstrip()+'$')
            f.close()
        except Exception as e:
            print(e)

# -T : option to display tab characters as ^I            
elif option=='-T':
    no_of_line=1
    for each_name in filename :
        try:
            f = open(each_name,'r')
            print("^I".join(f.read().split("\t")))		
            f.close()
        except Exception as e:
            print(e)

# -u : to display the content of file            
elif option=='-u':
    for each_name in filename :
        try:
            f = open(each_name,'r')
            for i in f:
                print(i.rstrip())
            f.close()
        except Exception as e:
            print(e)

# if option doesn't matches            
else:
    print("Enter a option like -n, -T, -E, -b or -u")

