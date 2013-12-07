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



#Roman numeral dictionary used to print the sequence in roman
numeral_map = zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
)

#Default invalid input error and exits
def defaultError(string):
    print 'ERROR:',string
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
        defaultError('Invalid Input.')
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
def fixBackSlash(string):
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
#converts a single char to its integer form
def charToInt(character):
    try:
        integer = ord(character)
    except:
        defaultError("1Invalid Input")
    return integer

#converts an integer to its char form
def intToChar(integer):
    try:
        character = ch(integer)
    except:
        defaultError('2')

#verifies that the argument is not an integer
def verifyChar(argument):
    holder = argument
    #Checks to see if the argument provided is an integer
    try:
        holder = int(argument)
    except:
        pass
    if isinstance(holder,int):
        defaultError('Invalid input. Input accepts single length characters.')
    return holder

    
#prints the alpha sequence baased on if it is upper case or lower case
def alphaSeq(lower,increment,upper):
    # [A-Z] = [65 - 90] 
    print lower, '/', increment,'/', upper
    if 65 <= lower <= 90 and 65<= upper <= 90:
        while lower <= upper:
            print chr(lower)
            lower = lower + increment
    # [a - z] = [97 - 122]
    elif 97 <= lower <= 122 and 97 <= upper <=122:
        while lower <= upper:
            print chr(lower)
            lower = lower + increment
    else:
        defaultError('Invalid character detected')

#checks to make sure that both arguments are upper case or lower case
def checkMismatchingBounds(lower,upper):
    if chr(upper).isupper() and chr(lower).isupper():
        pass
    elif chr(upper).islower() and chr(lower).islower():
        pass
    else:
       defaultError('Mismatch characters.')

#converts a positive, non-zero integer into a roman numeral string
def intToRoman(i):
    result = []
    if(i <= 0):
        defaultError('Integer must be positive and non-zero.')
    for integer, numeral in numeral_map:
        count = int(i / integer)
        result.append(numeral * count)
        i -= integer * count
    return ''.join(result)

#converts a roman numeral string to an integer. If it is not a valid roman numeral returns 0.
def romanToInt(n):
    n = unicode(n).upper()
    i = result = 0
    for integer, numeral in numeral_map:
        while n[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    return result
#prints the sequence in roman
def romanSeq(lower,increment,upper):
    while lower <= upper:
        print intToRoman(lower)
        lower += increment
    exit(1)


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
group.add_argument("--formatword","-F", help = "Prints the arguments as the format specificified[arabic,floating,alpha,roman].",action = "count")
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

#Handles the format word case
if args.formatword == 1:
    acceptableTypes = ['arabic','ARABIC','floating','FLOATING','alpha','ALPHA','roman','ROMAN']
    try:
        if str(argv[2])in acceptableTypes:
            formatType = str(argv[2]).lower()
    except:
        defaultError('Invalid formatword type. Accepted types: [arabic,floating,alpha,roman]')

    # Will find the formatType and assign the values for lower,increment and upper
    #[-F TYPE Upper]
    if len(argv) == 4:
        if formatType == 'arabic':
            upper = verifyArg(str(argv[3]),3)
            upper = int(upper)
            lower = __LOWER
            increment = __INCREMENT
        elif formatType == 'floating':
            upper = verifyArg(str(argv[3]),3)
            upper = float(upper)
            lower = float(__LOWER)
            increment = float(__INCREMENT)
        elif formatType == 'alpha':
            upper = verifyChar(str(argv[3]))
            upper = charToInt(upper)
            if chr(upper).isupper():
                lower = charToInt('A')
            else:    
                lower = charToInt('a')
            increment = 1
        elif formatType == 'roman':
            try:
                upper = int(argv[3])
                lower = __LOWER
                increment = __INCREMENT
            except:
                upper = str(argv[3]) 
                #checks for valid roman numeral     
                if romanToInt(upper) == 0:
                    defaultError('Invalid roman Numeral.')
                lower = intToRoman(__LOWER)
                increment = intToRoman(__INCREMENT)
    #[-F TYPE Lower Upper]
    elif len(argv) == 5:
        if formatType == 'arabic':
            lower = verifyArg(str(argv[3]),3)
            lower = int(lower)
            upper = verifyArg(str(argv[4]),4)
            upper = int(upper)
            increment = __INCREMENT
        elif formatType == 'floating':
            try:
                lower = float(str(argv[3]))
                upper = float(str(argv[4]))      
                increment = float(__INCREMENT)
            except:
                defaultError('Invalid character detected.')
        elif formatType == 'alpha':
            lower = verifyChar(str(argv[3]))
            upper = verifyChar(str(argv[4]))
            lower = charToInt(lower)
            upper = charToInt(upper)
            checkMismatchingBounds(lower,upper)
            increment = __INCREMENT
        elif formatType == 'roman':
            try:
                lower = int(argv[3])
                upper = int(argv[4])
                increment = 1
            except: 
                lower = str(argv[3])
                upper = str(argv[4])
                if romanToInt(upper) == 0 or romanToInt(lower) == 0:
                    defaultError('Mixed input. Must enter int, int or roman, roman.')
                increment = intToRoman(__INCREMENT)
    #[-F TYPE Lower Increment Upper]
    elif len(argv) == 6:
        if formatType == 'arabic':
            upper = verifyArg(str(argv[5]),5)
            upper = int(upper)
            lower = verifyArg(str(argv[3]),3)
            lower = int(lower)
            increment = verifyArg(str(argv[4]),4)
            increment = int(increment)
            verifyIncrement(increment)
        elif formatType == 'floating':
            try:
                lower = float(str(argv[3]))
                upper = float(str(argv[5]))
                increment = float(str(argv[4]))       
            except:
                defaultError('Invalid character detected.')
        elif formatType == 'alpha':
            lower = verifyChar(str(argv[3]))
            upper = verifyChar(str(argv[5]))
            try:
            	increment = int(str(argv[4]))
            except:
            	defaultError('Increment must be an integer')
            upper = charToInt(upper)
            lower = charToInt(lower)
            checkMismatchingBounds(lower,upper)
        elif formatType == 'roman':
            try:
                lower = int(argv[3])
                increment = int(argv[4])
                upper = int(argv[5])
            except:
                lower = str(argv[3])
                increment = str(argv[4])
                upper = str(argv[5])
                if romanToInt(upper) == 0 or romanToInt(lower) == 0 or romanToInt(increment) == 0:
                    defaultError('Mixed input. Must enter int, int, int or roman, roman, roman.')   
    else:
        defaultError('Too many arguments.')


    if formatType == 'alpha':
        alphaSeq(lower,increment,upper)
    elif formatType == 'roman':
        if isinstance(lower,int) and isinstance(increment,int) and isinstance(upper,int):
            romanSeq(lower,increment,upper)
        elif isinstance(lower,str) and isinstance(increment,str) and isinstance(upper,str):
            lower = romanToInt(lower)
            upper = romanToInt(upper)
            increment = romanToInt(increment)
            romanSeq(lower,increment,upper)
        else:
            defaultError('Mixed input.')
    else:
        printSeq(lower,increment,upper)
exit(1)


#Defines that variables based on the position of the argument.  
if args.separator == 1 or args.format == 1 or args.equalwidth == 1 or args.pad == 1 or args.padspaces == 1:

    formatTypes = ['\\n','\\t','\\a','\\f','\\r','\\v','\\\\']
    # Determines PadChar for -p/--pad 
    if args.pad == 1:
        string = str(argv[2])
	#checks to see if there is a format type that is being used as padding
        if string in formatTypes or len(string) == 1:
            padChar = string
        else:
            defaultError("Padding error. Try to put your pad character between quotes(i.e. '~'). NOTE: Length must equal 1.")


    #provides a flag without arguments following the flag [i.e. -f ]
    if len(argv) == 2:
        defaultError('Invalid Input.')
    #provides one argument after a flag [i.e. -f upper]
    elif len(argv) == 3:
	if args.pad == 1:
            defaultError('Invalid Input.')
            defaultError('Invalid Input.')
        upper = verifyArg(str(argv[2]),2)

	string = __STRING
        formatType = __FORMAT
	#Sets the proper default lower/increment variables [i.e. float/int]
        if isinstance(upper,float):
            lower = float(__LOWER)
	    increment = float(__INCREMENT)
	else:
	    lower = __LOWER
	    increment = __INCREMENT
    #provides two arguments after a flag [i.e. -f upper lower]
    elif len(argv) == 4:        
         #Handles the pad special case[i.e. -p 'a' upper]
         if args.pad == 1:
            upper = verifyArg(str(argv[3]),3)
            #Sets the proper default lower/increment variables [i.e. float/int]
            if isinstance(upper,float):
                increment = float(__INCREMENT)
                lower = float(__LOWER)
            else:
                increment = __INCREMENT
                lower = __LOWER
         elif args.separator == 1:
             upper = verifyArg(str(argv[3]),3)
             string = str(argv[2])
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
	    increment = __INCREMENT      
	#[i.e. -P upper inc lower]
	if args.padspaces == 1:
	    lower = verifyArg(str(argv[2]),2) 
	    increment = verifyArg(str(argv[3]),3)
    else:
	if args.pad == 1:
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
         print lower,fixBackSlash(string),
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
    fixedPadChar = fixBackSlash(padChar)
    printPad(lower,increment,upper,maxWidth,fixedPadChar)
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
            defaultError('Invalid Input.')
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
