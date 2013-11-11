# This program is a modified seq command called sequ. This source code will hose all 5 compliance levels. Compliance level 0 is due on 10/20/2013. Compliance level 1 is due on 11/11/2013
# Name: Justin Shuck
# Copy right (c) Justin Shuck


from sys import argv,exit
import numbers,argparse,sys

#Current version of sequ
__VERSION =  '1.0.0'


#will print the sequence that has a lower and upper bound and an increment.
def printSeq(lower,increment,upper):
    while lower <= upper:
        print(lower)
        lower = lower + increment 
#emulates the printf function that is used in C
def printf(format,*args):
    sys.stdout.write(format %args  )
    print

#Verifys the argument is an int. If the cast fails, it is not an int.
def verifyArg(argument,x):
    try:
        argument = int(str(argv[x]))
	return argument
    except ValueError:
	pass
    try:
	argument = float(str(argv[x]))
	return argument
    except ValueError:
        print "1.Error: Invalid input"
    	exit(1)

# Define arguments that are handled in this program
parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()

group.add_argument("--version","-v", help="View the current version of sequ", action="count")
group.add_argument("--separator","-s", help="Seperate the sequence by a string", action="count")
group.add_argument("--format","-f", help = "Uses Floating-point Format",action = "count")
group.add_argument("--equalwidth","-w", help = "Equalies the width by adding leading zeros", action = "count")

#Postionals
parser.add_argument("string", nargs="?", default= " ",help = "A string that will seperate the numbers in the sequence")
parser.add_argument("lower", nargs = "?", help = "Lower bounds of the sequence")
parser.add_argument("upper", nargs = "?", help = "Upper bounds of the sequence")

args = parser.parse_args()

#The definition of Arguments
if args.version == 1:
    print"SEQU Version "+__VERSION
    exit(1)

#-s and --separator
if args.separator == 1:
    #If the form is of 'sequ.py -s 1 10' i.e no position after -s flag
    if len(argv) ==4:
	#verify if the variables are in the proper position
	lower = verifyArg(str(argv[2]),2)
	upper = verifyArg(str(argv[3]),3)
        string = "\n"		#default string separator
    #The string is present after the -s flag
    else:
        lower = verifyArg(str(argv[3]),3)
        upper = verifyArg(str(argv[4]),4)
        string = str(argv[2])   
    #Prints the sequence with the string as a separator
    while lower <= upper:
        print lower, string,
        lower+=1       
    
    exit(1)

#-f and --format
if args.format == 1:
    #No positional after the -f flag
    if len(argv) == 4:
	#verify if the variables are in the proper position
        lower = verifyArg(str(argv[2]),2)
        upper = verifyArg(str(argv[3]),3)
        formatType = "%g"	#default format type

	#Prints the sequence with the printf function
        while lower <= upper:
	    printf(formatType,lower)
	    lower+=1
	exit(1)

    else:
        lower = verifyArg(str(argv[3]),3)
        upper = verifyArg(str(argv[4]),4)
	formatType = str(argv[2])
    
	#Accepted format types that this program accepts
	accepted = {'%g','%X','%e','%f'}

	#Prints if the user entered a proper format type, otherwise exit
	if formatType in accepted:
            while lower <= upper:
                printf(formatType,lower)
                lower+=1
	    exit(1)
        else:
 	    print 'Error: Invalid format Type.'
	    exit(1)	

#-w and --equalwidth
if args.equalwidth == 1:
    #Verifys if there is an increment variable ( Lower, Increment, Upper)
    if len(argv) == 4:
         lower = verifyArg(str(argv[2]),2)
         upper = verifyArg(str(argv[3]),3)
	 increment = 1			#Default increment is 1
	 maxWidth = len(str(argv[3]))	#Gets the Max Width from the Upper argument
    else:
	 lower = verifyArg(str(argv[2]),2)
	 upper = verifyArg(str(argv[4]),4)
	 increment = verifyArg(str(argv[3]),3)
         maxWidth = len((argv[4]))	#Gets the Max Width from the Upper argument

    #Prints the sequence with equal width using zfill
    while lower <= upper:
         print str(lower).zfill(maxWidth)
	 lower = lower+increment

    exit(1)


# Used to verify that there is not more than 2 arguments(besides the file)
if len(argv) <= 2 or len(argv) > 6:
    print('Error: Invalid number of arguments.')
    exit(1)


#Checks to verify that the arguments are both integers. will terminate with an error if one of the arguments is bad.
if len(argv) >= 3:

    lower = verifyArg(str(argv[1]),1)
    upper = verifyArg(str(argv[2]),2)
    #if there is an increment variable(lower,increment,upper)
    if len(argv) == 4:
        upper = verifyArg(str(argv[3]),3)
        increment = verifyArg(str(argv[2]),2)
    else: 
        increment = 1	#defaults increment at 1

    printSeq(lower,increment,upper)
