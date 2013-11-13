# This program is a modified seq command called sequ. This source code will hose all 5 compliance levels. Compliance level 0 is due on 10/20/2013. Compliance level 1 is due on 11/11/2013
# Name: Justin Shuck
# Copy right (c) Justin Shuck


from sys import argv,exit
import numbers,argparse,sys

#Current version of sequ
__VERSION =  '1.0.0'


#Default invalid input error and exit
def invalidInput():
    print 'Error: Invalid Input.'
    exit(1)

#will print the sequence that has a lower and upper bound and an increment.
def printSeq(lower,increment,upper):
    while lower <= upper:
        print(lower)
        lower = lower + increment 

#emulates the printf function that is used in C
def printf(format,*args):
    sys.stdout.write(format %args )
    print

#Verifys the argument is an int. If the cast fails, it is not an int, it then trys to cast to a float. If it is neither the program terminates
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
        invalidInput()
    	exit(1)

#will go through the sequence and find the max width and return it
def findMaxWidth(lower,inc,upper):
    maxWidth = 0
    while lower <= upper:
	if len(str(lower)) > maxWidth:
	    maxWidth = len(str(lower))
        lower = lower + inc
	if inc == 0:
	    return maxWidth
    return maxWidth

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

#-s and --separator, the default string separator is ""
if args.separator == 1:
    #has nothing after the -s flag
    if len(argv) == 2:
        invalidInput()
    #has one argument after the -s flag
    if len(argv) == 3:
        upper = verifyArg(str(argv[2]),2)
	lower = 1
        string = ""
    #has two arguments after the -s flag
    elif len(argv) == 4:
	lower = verifyArg(str(argv[2]),2)
	upper = verifyArg(str(argv[3]),3)
        string = ""		
    #has three arguments after the -s flag. (string, lower, upper)
    else:
        lower = verifyArg(str(argv[3]),3)
        upper = verifyArg(str(argv[4]),4)
        string = str(argv[2])   

    #Prints the sequence with the string as a separator and then exits
    while lower <= upper:
        print lower
	print string
        lower+=1       
    exit(1)

#-f and --format, the default format is '%g'
if args.format == 1:
    #nothing after the -f flag
    if len(argv) == 2:
        invalidInput()
    #One argument after the -f flag
    if len(argv) == 3:
        upper = verifyArg(str(argv[2]),2)
        lower = 1
	formatType = "%g"
    #Two arguments after the -f flag
    elif len(argv) == 4:
        lower = verifyArg(str(argv[2]),2)
        upper = verifyArg(str(argv[3]),3)
        formatType = "%g"
    #has three arguments after the -f flag. (format,lower,upper)
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

#-w and --equalwidth, default width is 1
if args.equalwidth == 1:
    #Nothing after the -w flag
    if len(argv) == 2:
	invalidInput()
    #One argument after the -w flag
    if len(argv) == 3:
         lower = 1
         upper = verifyArg(str(argv[2]),2)
         increment = 1
         maxWidth = findMaxWidth(0,1,verifyArg(str(argv[2]),2))
    #Two arguments after the -w flag
    elif len(argv) == 4:
         lower = verifyArg(str(argv[2]),2)
         upper = verifyArg(str(argv[3]),3)
	 increment = 1
	 maxWidth = findMaxWidth(verifyArg(str(argv[2]),2),1,verifyArg(str(argv[3]),3))
    #Has three arguments after the -w flag. (lower,increment,upper)
    else:
	 lower = verifyArg(str(argv[2]),2)
	 upper = verifyArg(str(argv[4]),4)
	 increment = verifyArg(str(argv[3]),3)
         maxWidth = findMaxWidth(verifyArg(str(argv[2]),2),verifyArg(str(argv[3]),3),verifyArg(str(argv[4]),4))

    #Prints the sequence with equal width using zfill
    while lower <= upper:
         print str(lower).zfill(maxWidth)
	 lower = lower+increment
    exit(1)


# Used to verify Invalid number of arguments
if len(argv) <= 1 or len(argv) > 6:
    print('Error: Invalid number of arguments.')
    exit(1)


#This will be used if there are no flags in front of the numbers if no increment is given the default is 1
if len(argv) == 2:
    try:
	int(str(argv[1]))
        lower = 1
	increment = 1
    except:
	try:
	    float(str(argv[1]))
            lower = 1.0
	    increment = 1.0
        except:
            invalidInput()
    upper = verifyArg(str(argv[1]),1)
#if there is not
if len(argv) >= 3:

    lower = verifyArg(str(argv[1]),1)
    upper = verifyArg(str(argv[2]),2)
    #if there is an increment variable(lower,increment,upper)
    if len(argv) == 4:
        upper = verifyArg(str(argv[3]),3)
        increment = verifyArg(str(argv[2]),2)
    else: 
        increment = 1
printSeq(lower,increment,upper)
