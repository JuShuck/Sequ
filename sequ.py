# This program is a modified seq command called sequ. This source code will hose all 5 compliance levels. Compliance level 0 is due on 10/20/2013.
# Name: Justin Shuck
# Copy right  Justin Shuck


from sys import argv,exit
import numbers,argparse


# Used to verify that there is not more than 2 arguments(besides the file)
if len(argv) != 3:
    print('Error: Invalid number of arguments.')
    exit(1)


#Checks to verify that the arguments are both integers. will terminate with an error if one of the arguments is bad.
try:
#cast the arguments to int types
    a = int(str(argv[1]))
    b = int(str(argv[2]))
except ValueError:
    print("Error: Invalid argument type")
    exit(1)
#If the arguments are the same
if a == b:
   print(a)
#If the 2nd argument is smaller than the first it will print in ascending order
if b > a:
    for x in range (a,b+1):
        print(x)

#If the 2nd argument is larger than the first, it will print in descending order
if b < a:
    while b <= a:
        print(a)
        a -= 1
