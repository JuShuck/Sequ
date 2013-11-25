	# This program is a modified seq command called sequ. This source code will hose all 5 compliance levels. Compliance level 0 is due on 10/20/2013. Compliance level 1 is due on 11/11/2013
# Name: Justin Shuck
# Copy right (c) Justin Shuck


from sys import argv,exit
import numbers,argparse,sys,string

# Constants used in the program (Default values)
__VERSION =  '1.0.0'
__STRING = " "
__LOWER = 1
__INCREMENT = 1
__FORMAT = "%g"
__F_LOWER = 1.0
__F_INCREMENT = 1.0


#Default invalid input error and exits
def invalidInput():
    print 'Error: Invalid Input.'
    exit(1)

#Handles the invalid pad character error and exits
def invalidPadChar():
    print "Error: Padding error. Try to put your pad character between quotes(i.e. '~'). NOTE: Length must equal 1."
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

#will verify that the increment is positive, if negative the program exits
def verifyIncrement(increment):
    if increment <= 0:
        print 'Error: Increment must be positive and non-zero.'
        exit(1)

#will go through the sequence and find the max width and return it
def findMaxWidth(lower,inc,upper):
    maxWidth = 0
    if inc == 0:
	return maxWidth

    while lower <= upper:
	if len(str(lower)) > maxWidth:
	    maxWidth = len(str(lower))
        lower = lower + inc
    return maxWidth

#will print a sequence with a pad using rjust.
def printPad(lower,increment,upper,maxWidth,padChar):
    while lower <= upper:
        print str(lower).rjust(maxWidth,padChar)
        lower = lower+increment
#Turns any backslash argument into its form
def backSlash(string):
    backSlashN = string.replace('\\n','\n') 
    backSlashT = backSlashN.replace('\\t','\t')
    backSlashA = backSlashT.replace('\\a','\a')
    backSlashF = backSlashA.replace('\\f','\f')
    backSlashR = backSlashF.replace('\\r','\r')
    backSlashV = backSlashR.replace('\\v','\v')
    backSlash = backSlashV.replace('\\\\','\\')
    return backSlash
#the implementation for -W/--words. seperates the string and pringts the new string
def wordsImplementation(word):
    stringWord = str(word)
    wordLen = len(word) -1
    finalString = ""
    for x in range(0,wordLen):
        finalString += stringWord[x]
        finalString += " "
    finalString += stringWord[wordLen]
    print finalString
    return


# Define arguments that are handled in this program
parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()

group.add_argument("--version","-v", help="View the current version of sequ", action="count")
group.add_argument("--separator","-s", help="Seperate the sequence by a string", action="count")
group.add_argument("--format","-f", help = "Uses Floating-point Format",action = "count")
group.add_argument("--equalwidth","-w", help = "Equalies the width by adding leading zeros", action = "count")
group.add_argument("--words","-W", help = "Prints the sequence on a single line", action = "count")
group.add_argument("--pad","-p", help = "Output the sequence with a single-char pad string.",action = "count")
group.add_argument("--padspaces","-P", help = "Output the sequence with spaces on the left to be all equal width.",action = "count")
#Postionals
parser.add_argument("string", nargs="?", default= " ",help = "A string that will seperate the numbers in the sequence")
parser.add_argument("lower", nargs = "?", help = "Lower bounds of the sequence")
parser.add_argument("upper", nargs = "?", help = "Upper bounds of the sequence")
parser.add_argument("increment", nargs = "?", help = "Increment of the sequence")

args = parser.parse_args()
    
#The definition of Arguments
if args.version == 1:
    print"SEQU Version "+__VERSION
    exit(1)

#Defines that variables based on the position of the argument.  
if args.separator == 1 or args.format == 1 or args.equalwidth == 1 or args.pad == 1 or args.padspaces == 1:
    #provides a flag without arguments following the flag [i.e. -f ]
    if len(argv) == 2:
        invalidInput()
    #provides one argument after a flag [i.e. -f upper]
    elif len(argv) == 3:
	if args.pad == 1:
	    invalidInput()
        upper = verifyArg(str(argv[2]),2)

	string = __STRING
        formatType = __FORMAT
	#Sets the proper default lower/increment variables [i.e. float/int]
        if isinstance(upper,float):
            lower = __F_LOWER
	    increment = __F_INCREMENT
	else:
	    lower = __LOWER
	    increment = __INCREMENT
    #provides two arguments after a flag [i.e. -f upper lower]
    elif len(argv) == 4:        
         #Handles the pad special case[i.e. -p 'a' upper]
         if args.pad == 1:
            upper = verifyArg(str(argv[3]),3)
            if len(str(argv[2])) > 1:
                invalidPadChar()
            else:
                padChar = str(argv[2])
		#Sets the proper default lower/increment variables [i.e. float/int]
		if isinstance(upper,float):
		     increment = __F_INCREMENT
		     lower = __F_LOWER
                else:
		     increment = __INCREMENT
		     lower = __LOWER
         else:
             increment = __INCREMENT
             lower = verifyArg(str(argv[2]),2)
             upper = verifyArg(str(argv[3]),3)
             string = __STRING
             formatType = __FORMAT

    #three arguments after a flag, will vary based on what flag
    elif len(argv) == 5:
	lower = verifyArg(str(argv[3]),3)
        upper = verifyArg(str(argv[4]),4)
        #[i.e. -s string lower upper]
	if args.separator == 1:
            string = str(argv[2])
        #[i.e. -f format lower upper]
        if args.format == 1:
            formatType = str(argv[2])
        #[i.e. -w lower increment upper] or [i.e. -W lower increment upper]
        if args.equalwidth == 1 or args.words == 1:
	    lower = verifyArg(str(argv[2]),2)
	    increment = verifyArg(str(argv[3]),3)
	    verifyIncrement(increment)
            upper = verifyArg(str(argv[4]),4)
	#[i.e. -p 'a' upper lower]
	if args.pad == 1:
	    if len(str(argv[2])) != 1:
	        invalidPadChar()
	    else:
	        padChar = str(argv[2])
	        increment = __INCREMENT       
	#[i.e. -P upper inc lower]
	if args.padspaces == 1:
	    lower = verifyArg(str(argv[2]),2) 
	    increment = verifyArg(str(argv[3]),3)
    else:
	if args.pad == 1:
	    if len(str(argv[2])) != 1:
	        invalidPadChar()
            else:
	        padChar = str(argv[2])
		lower = verifyArg(str(argv[3]),3)
	        increment = verifyArg(str(argv[4]),4)
		verifyIncrement(increment)
		upper = verifyArg(str(argv[5]),5)
	else:
	    print 'Error: Too many arguments entered'
	    exit(1)
	    

#-s and --separator, the default string separator is ""
if args.separator == 1:
    while lower <= upper:
         print lower,backSlash(string),
         lower+=1
    exit(1)
  

#-f and --format, the default format is '%g'
if args.format == 1: 
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
    # Finds the max width of the sequence
    maxWidth = findMaxWidth(lower,increment,upper)

    #Prints the sequence with equal width using zfill
    while lower <= upper:
         print str(lower).zfill(maxWidth)
	 lower = lower+increment
    exit(1)

#-W and --words
if args.words == 1:
    argLen = len(argv)
    #Prints all the arguments in proper form
    for x in range(2,argLen):
        word = str(argv[x])
        wordsImplementation(word)
    exit(1)

#-p and --pad
if args.pad == 1:
    #Finds the max width of the sequence
    maxWidth = findMaxWidth(lower,increment,upper)
    printPad(lower,increment,upper,maxWidth,padChar)
    exit(1)

#-P and --padspaces
if args.padspaces == 1:
    #Finds max width of the sequence
    maxWidth = findMaxWidth(lower,increment,upper)
    printPad(lower,increment,upper,maxWidth,' ')
    exit(1)

# Used to verify Invalid number of arguments
if len(argv) <= 1 or len(argv) >= 5:
    print('Error: Invalid number of arguments.')
    exit(1)


#This will be used if there are no flags in front of the numbers if no increment is given the default is 1
if len(argv) == 2:
    try:
	int(str(argv[1]))
        lower = __LOWER
	increment = __INCREMENT
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
    #if there is an increment variable(lower,increment,upper)
    if len(argv) == 4:
        upper = verifyArg(str(argv[3]),3)
        increment = verifyArg(str(argv[2]),2)
	verifyIncrement(increment)
    else: 
        increment = __INCREMENT
        upper = verifyArg(str(argv[2]),2)

printSeq(lower,increment,upper)
