# This program is a modified seq command called sequ. This source code will hose all 5 compliance levels.
# Copy right (c) Justin Shuck


from sys import argv,exit
import numbers,argparse,sys,string,math

# Constants used in the program (Default values)
__VERSION =  '1.0.0'
__STRING = " "
__LOWER = 1
__INCREMENT = 1
__FORMAT = "%g"
__SEPARATOR = ' '

#Roman numeral dictionary used to print the sequence in roman
#Credit for roman numerial implementation Tim Valenta [code.activestate.com/recipes/81611-roman-numerals/]
numeral_map = zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
)

#Verifys if the argument passed in is an int. True = integer, False = Not integer
def isInt(num):
    try:
        num = int(num)
        return True
    except:
        return False

#Verifys if the argument passed in is a float OR int. True = float,int, False = Not float,int
def isFloat(num):
    try:
        num = float(num)
        return True
    except:
        return False

#Default invalid input error and exits
def defaultError(string):
    print 'ERROR:',string
    exit(1)

#will print the sequence that has a lower and upper bound and an increment.
def printSeq(lower,increment,upper):
    while lower <= upper:
        print(lower)
        lower = lower + increment 
    exit(1)

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
    if increment <= 0.0:
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
# Credit for help: Souriya Khaosanga
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
        defaultError("Invalid Input")
    return integer

#converts an integer to its char form
def intToChar(integer):
    try:
        character = ch(integer)
    except:
        defaultError('Invalid Input.')

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
    #print lower, '/', increment,'/', upper 		#Used to see the integer values of the variables passed into alphaSeq
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
    exit(1)

#Used to find the other 'bound' of a given char input. Will ensure that the sequence is all in upper-case or lower-case
def findOtherBound(boundOne):
    if chr(boundOne).isupper():
        boundTwo = charToInt('A')
    else:    
        boundTwo = charToInt('a')
    return boundTwo

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

#Handles the roman instances(i.e. mixed roman/int input)    
def computeRoman(lower,increment,upper):
       #Assigns the integer representation of the lower
    if isInt(lower):
        lower = int(lower)
    elif romanToInt(lower) != 0:
        lower = romanToInt(lower)
    else:
        defaultError('Invalid roman character in input')
     #Assigns the integer representation of the increment
    if isInt(increment):
        increment = int(increment)
    elif romanToInt(increment) != 0:
        increment = romanToInt(increment)
    else:
        defaultError('Invalid roman character in input')
    #Assigns the integer representation of the upper
    if isInt(upper):
        upper = int(upper)
    elif romanToInt(upper) != 0:
        upper = romanToInt(upper)
    else:
        defaultError('Invalid roman character in input')
    romanSeq(lower,increment,upper)
#Puts the lines of a file into a list. If the file is not found the program terminates early
def putLinesInList(fi):
    try:
        with open(fi) as f:
            resultingList = f.read().splitlines()
    	return resultingList
    except:
    	defaultError('File not found.')

#Prints the lines of the file with an arabic or floating sequence
def printFileSeq(lower,increment,lineList,separator):
    #Finds the max width of the last sequence number
    listLen = len(lineList)-1
    largest = lower
    while listLen > 0:
        listLen -= 1
        largest +=increment
    maxWidth = len(str(largest))
    for first,line in enumerate(lineList):
        print str(lower).rjust(maxWidth,' '),separator,line
        lower +=increment
    exit(1)

#Prints the lines of the file with an alpha sequence
def printFileAlphaSeq(lower,increment,lineList,separator):
    #Finds the max width of the last sequence number
    maxWidth = 1
    if not isInt(increment):
        defaultError('Increment must be an integer')
    #Flag will be used to keep track if the char is Upper-case or Lower-case. True = Upper, False = Lower
    flag = False
    if chr(lower).isupper():
        flag = True
    for first,line in enumerate(lineList):
        print str(chr(lower)).rjust(maxWidth,' '),separator,line
        lower +=increment
        #Resets the alpha seq. flag = True means [A-Z], flag = False [a - z]
        if flag:
            if lower > 90:
                lower = 65
        if not flag:
            if lower > 122:
                lower = 97
    exit(1)

#Prints the lines of the file with a roman sequence
def printFileRomanSeq(lower,increment,lineList,separator):
    listLen = len(lineList)
    lowCopy = lower
    result = []
    while listLen > 0:
        listLen -= 1
        result.append(intToRoman(lowCopy))
        lowCopy += increment
    maxlength = max(len(s) for s in result)
    for first,line in enumerate(lineList):
        print str(intToRoman(lower)).rjust(maxlength,' '),separator,line
        lower +=increment
    exit(1)

#Handles the cases that include a specific formatType. [i.e. FORMAT FILE lower increment separator]
def determineWithFormatType(formatType,lower,increment,separator,fileList):
    #Integer
    if formatType == 'arabic':
        if isFloat(lower) and isFloat(increment):
            verifyIncrement(int(math.floor(float(increment))))
            printFileSeq(int(math.floor(float(lower))),int(math.floor(float(increment))),fileList,separator)
        else:
            defaultError('Invalid Input.')
    #Float
    if formatType == 'floating':
        if isFloat(lower) and isFloat(increment):
            verifyIncrement(float(increment))
            printFileSeq(float(lower),float(increment),fileList,separator)
        else:
            defaultError('Invalid Input.')
    if formatType == 'alpha':
        #Verifys that lower is [A-Z] or [a-z]
        if len(lower) != 1 or ord(lower) < 65 or ord(lower) > 90 and ord(lower) < 97 or ord(lower) > 122:
            defaultError('Invalid Input.')
        if not isInt(increment):
            defaultError('Invalid Input.')
        printFileAlphaSeq(charToInt(lower),int(increment),fileList,separator)
    if formatType == 'roman':
        #Assigns the lower correctly
        if isInt(lower):
            lower = int(lower)
        elif romanToInt(lower) != 0:
            lower = romanToInt(lower)
        else:
            defaultError('Invalid roman character in input')
        #Assigns the increment correctly
        if isInt(increment):
            increment = int(increment)
        elif romanToInt(increment) != 0:
            increment = romanToInt(increment)
        else:
            defaultError('Invalid roman character in input')
        verifyIncrement(increment)
        printFileRomanSeq(lower,increment,fileList,separator)
    defaultError('Invalid Input.')

#Handles the case that doesnt have an implicit format type [i.e. FILE lower increment separator]
def determine(lower,increment,separator,fileList):
    #Integer
    if isInt(lower) and isInt(increment):
        printFileSeq(int(lower),int(increment),fileList,separator)
    #Float
    elif isFloat(lower) and isFloat(increment):
        printFileSeq(float(lower),float(increment),fileList,separator)
    #Alpha
    elif len(lower) == 1 and not isInt(lower) and not isFloat(lower):
        if isInt(increment):
            verifyIncrement(int(increment))
            printFileAlphaSeq(charToInt(lower),int(increment),fileList,separator)
        else:
            defaultError('Increment must be a positive,non-zero integer.')
    #Roman
    elif romanToInt(lower) != 0 or romanToInt(increment) != 0:
        if romanToInt(increment) == 0:
            if isInt(increment):
                printFileRomanSeq(romanToInt(lower),int(increment),fileList,separator)
            else:
                defaultError('Invalid Input')
        elif romanToInt(lower) == 0 and isInt(lower):
            printFileRomanSeq(int(lower),romanToInt(increment),fileList,separator)
        else:
            printFileRomanSeq(romanToInt(lower),romanToInt(increment),fileList,separator)
    else:
        defaultError('Invalid Input.') 



# Define arguments that are handled in this program
parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()

group.add_argument("--version","-v", help="View the current version of sequ", action="count")
parser.add_argument("--separator","-s", help="Seperate the sequence by a string", action="count")
group.add_argument("--format","-f", help = "Uses Floating-point Format",action = "count")
group.add_argument("--equalwidth","-w", help = "Equalies the width by adding leading zeros", action = "count")
group.add_argument("--words","-W", help = "Prints the sequence on a single line", action = "count")
group.add_argument("--pad","-p", help = "Output the sequence with a single-char pad string.",action = "count")
group.add_argument("--padspaces","-P", help = "Output the sequence with spaces on the left to be all equal width.",action = "count")
parser.add_argument("--formatword","-F", help = "Prints the arguments as the format specificified[arabic,floating,alpha,roman].",action = "count")
parser.add_argument("--numberlines","-n",help = "Prints the contents of a file numbered with parameters entered.( [FORMAT][FILE][lower][increment][separator] )",action = "count")

#Postionals
parser.add_argument("string", nargs="?", default= " ",help = "A string that will seperate the numbers in the sequence")
parser.add_argument("lower", nargs = "?", help = "Lower bounds of the sequence")
parser.add_argument("upper", nargs = "?", help = "Upper bounds of the sequence")
parser.add_argument("increment", nargs = "?", help = "Increment of the sequence")
parser.add_argument("format", nargs = "?", help = "The format for the --formatwords")

args = parser.parse_args()

#The definition of Arguments
if args.version == 1:
    print"SEQU Version "+__VERSION
    exit(1)

#Handles the number lines arguments
if args.numberlines == 1:
    #Throws out bad input
    if len(argv) <=2 or len(argv) > 8:
        defaultError('Invalid number of arguments.')
    #Will be used to check if the type selected is an acceptable type for format-word. 
    acceptableTypes = ['arabic','ARABIC','floating','FLOATING','alpha','ALPHA','roman','ROMAN']
    #[-n FILE] 
    if len(argv) == 3:
        fileList = putLinesInList(argv[2])
        printFileSeq(__LOWER,__INCREMENT,fileList,__SEPARATOR)
    #[-n TYPE FILE] or [-n FILE lower]
    if len(argv) == 4:
        #[-n TYPE FILE]
        if str(argv[2]).lower() in acceptableTypes:
            formatType = str(argv[2]).lower()
            fileList = putLinesInList(argv[3])
            if formatType == 'arabic':
                printFileSeq(__LOWER,__INCREMENT,fileList,__SEPARATOR)
            if formatType == 'floating':
                printFileSeq(float(__LOWER),float(__INCREMENT),fileList,__SEPARATOR)
            if formatType == 'alpha':
                printFileAlphaSeq(charToInt('a'),__INCREMENT,fileList,__SEPARATOR)
            if formatType == 'roman':
                printFileRomanSeq(__LOWER,__INCREMENT,fileList,__SEPARATOR)
        else:
            #[-n FILE lower]
            fileList = putLinesInList(argv[2])
            lower = str(argv[3])
            determine(lower,__INCREMENT,__SEPARATOR,fileList)
    #[-n TYPE FILE lower] or [-n FILE lower increment]
    if len(argv) == 5:
        #[-n TYPE FILE lower]        
        if str(argv[2]).lower() in acceptableTypes:
            formatType = str(argv[2]).lower()
            fileList = putLinesInList(argv[3])
            lower = str(argv[4])
            determineWithFormatType(formatType,lower,__INCREMENT,__SEPARATOR,fileList)
        #[-n FILE lower increment]
        else:
            fileList = putLinesInList(argv[2])
            lower = str(argv[3])
            increment = str(argv[4])
            determine(lower,increment,__SEPARATOR,fileList)           
    #[-n TYPE FILE lower increment] and [-n FILE lower increment seperator]
    if len(argv) == 6:
    #[-n TYPE FILE lower increment]
        if str(argv[2]).lower() in acceptableTypes:
            formatType = str(argv[2]).lower()
            fileList = putLinesInList(argv[3])
            lower = str(argv[4])
            increment = str(argv[5])
            determineWithFormatType(formatType,lower,increment,__SEPARATOR,fileList)
        #[-n FILE lower increment seperator]
        else:
            fileList = putLinesInList(argv[2])
            lower = str(argv[3])
            increment = str(argv[4])
            separator = str(argv[5])
            determine(lower,increment,separator,fileList)
    #[-n TYPE FILE lower increment seperator]
    if len(argv) == 7:
        if str(argv[2]).lower() in acceptableTypes:
            formatType = str(argv[2]).lower()
            fileList = putLinesInList(argv[3])
            lower = str(argv[4])
            increment = str(argv[5])
            separator = str(argv[6])
            determineWithFormatType(formatType,lower,increment,separator,fileList)
        else:
            defaultError('Invalid Input.')

#Handles the format word case
if args.formatword == 1:
    #Verifys that there are a correct number of arguments
    if len(argv) <= 3 or len(argv) > 6:
        defaultError('Invalid number of Arguments')

    #Will check to see if the type selected is an acceptable type for format-word. 
    acceptableTypes = ['arabic','ARABIC','floating','FLOATING','alpha','ALPHA','roman','ROMAN']

    if str(argv[2]).lower() in acceptableTypes:
        formatType = str(argv[2]).lower()
    else:
        defaultError('Invalid formatword type. Accepted types: [arabic,floating,alpha,roman] NOTE: -n TYPE FILE')
    # Will find the formatType and assign the values for lower,increment and upper
    #[-F TYPE Upper]
    if len(argv) == 4:
        upper = str(argv[3])
        determineWithFormatType
        if formatType == 'arabic':
            if isFloat(upper):
                upper = math.floor(float(upper))
                printSeq(__LOWER,__INCREMENT,int(math.floor(upper)))
        elif formatType == 'floating':
            if isInt(upper) or isFloat(upper):
                printSeq(float(__LOWER),float(__INCREMENT),float(upper))
        elif formatType == 'alpha':
            lower = findOtherBound(charToInt(upper))
            alphaSeq(lower,__INCREMENT,charToInt(upper))
        elif formatType == 'roman':
            computeRoman(__LOWER,__INCREMENT,upper)
        defaultError('Invalid Input.')
    #[-F TYPE Lower Upper]
    if len(argv) == 5:
        lower = str(argv[3])
        upper = str(argv[4])
        if formatType == 'arabic':
            if isFloat(lower) and isFloat(upper):
                upper = math.floor(float(upper))
                lower = math.floor(float(lower))
                printSeq(int(lower),__INCREMENT,int(upper))
        elif formatType == 'floating':
            if isFloat(lower) and isFloat(upper):
                printSeq(float(lower),float(__INCREMENT),float(upper))
        elif formatType == 'alpha':
            if len(upper) == 1 and len(lower) == 1 and not isInt(upper) and not isInt(lower):
                checkMismatchingBounds(charToInt(lower),charToInt(upper))
                alphaSeq(charToInt(lower),__INCREMENT,charToInt(upper))
        elif formatType == 'roman':
            computeRoman(lower,__INCREMENT,upper)
        defaultError('Invalid Input.')
    #[-F TYPE Lower Increment Upper]
    if len(argv) == 6:
        lower = str(argv[3])
        increment = str(argv[4])
        upper = str(argv[5])
        if formatType == 'arabic':
            if isFloat(lower) and isFloat(increment) and isFloat(upper):
                lower = math.floor(float(lower))
                increment = math.floor(float(increment))
                upper = math.floor(float(upper))
                verifyIncrement(int(increment))
                printSeq(int(lower),int(increment),int(upper))
        elif formatType == 'floating':
            if isFloat(lower) and isFloat(increment) and isFloat(upper):
                verifyIncrement(float(increment))
                printSeq(float(lower),float(increment),float(upper))
        elif formatType == 'alpha':
            if len(lower) == 1 and len(upper) == 1 and isInt(increment) and not isInt(upper) and not isInt(lower):
                checkMismatchingBounds(charToInt(lower),charToInt(upper))
                verifyIncrement(int(increment))
                alphaSeq(charToInt(lower),int(increment),charToInt(upper))
        elif formatType == 'roman':
            #Assigns the integer representation of the lower
            computeRoman(lower,increment,upper)
        defaultError('Invalid Input.')


#This will assign the variables needed to print the users request.
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
    #provides two arguments after a flag[i.e. -f lower upper]
    elif len(argv) == 4:       
        upper = verifyArg(str(argv[3]),3)
        #Handles the pad special case[i.e. -p 'a' upper]
        if args.pad == 1:
            #Sets the proper default lower/increment variables [i.e. float/int]
            if isinstance(upper,float):
                increment = float(__INCREMENT)
                lower = float(__LOWER)
            else:
                increment = __INCREMENT
                lower = __LOWER
	 #Handles the separator specal case[i.e. -s string upper]
        elif args.separator == 1:
            string = str(argv[2])
            lower = __LOWER
         #Handles the format special case[i.e. -f lower upper AND -f FORMAT upper]
        elif args.format == 1:
            lower = __LOWER
            formatType = str(argv[2])
            if isInt(formatType):
                lower = int(formatType)
                formatType = __FORMAT
            elif isFloat(formatType):
                lower = float(formatType)
                formatType = __FORMAT
        else:
            increment = __INCREMENT
            lower = verifyArg(str(argv[2]),2)
            upper = verifyArg(str(argv[3]),3)

    #three arguments after a flag, will vary based on what flag
    elif len(argv) == 5:
	lower = verifyArg(str(argv[3]),3)
        upper = verifyArg(str(argv[4]),4)
        #[i.e. -s string lower upper]
	if args.separator == 1:
            string = str(argv[2])
        #[i.e. -f format lower upper AND -f lower increment upper]
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
            defaultError('Invalid Input')
	    
#Below is the printing implementation for the flag inputs.
#The statement above assigns the proper values for the variables for the statements below
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
        defaultError('Invalid format type')

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

# With no flags, the range of length is 2 - 4.
if len(argv) <= 1 or len(argv) >= 5:
    defaultError('Invalid number of arguments.')
#If there are no flags then we must determine the input and print the sequence.
#Valid sequences: Integers,Floats,Alpha and Roman. Alpha has presidence over roman.
#[upper]
if len(argv) == 2:
    upper = str(argv[1])
    #Integer input
    if isInt(upper):
        printSeq(__LOWER,__INCREMENT,int(upper))
    #Floating input
    if isFloat(upper):
        printSeq(float(__LOWER),float(__INCREMENT),float(upper))
    #Alpha input
    if len(upper) == 1 and not isInt(upper) and not isFloat(upper):
        alphaSeq(findOtherBound(charToInt(upper)),__INCREMENT,charToInt(upper))
    #Roman input
    if romanToInt(upper) != 0:
        romanSeq(__LOWER,__INCREMENT,romanToInt(upper))
    defaultError('Invalid Input.')
#[lower upper]
elif len(argv) == 3:
    lower = str(argv[1])
    upper = str(argv[2])
    increment = __INCREMENT
    #Integer input
    if isInt(lower) and isInt(upper):
        printSeq(int(lower),__INCREMENT,int(upper))
    #Floating input
    if isFloat(lower) and isFloat(upper):
       printSeq(float(lower),__INCREMENT,float(upper))
    #Alpha input
    if len(upper) == 1 and len(lower) == 1 and not isInt(upper) and not isInt(lower):
        checkMismatchingBounds(charToInt(lower),charToInt(upper))
        alphaSeq(charToInt(lower),__INCREMENT,charToInt(upper))
    #Roman input
    if (romanToInt(lower)+1) != 0 and (romanToInt(upper)+1) != 0:
        romanSeq(romanToInt(lower),__INCREMENT,romanToInt(upper))
    defaultError('Invalid Input.')
#[lower increment upper]
elif len(argv) == 4:
    lower = str(argv[1])
    increment = str(argv[2])
    upper = str(argv[3])
    #Integer input
    if isInt(lower) and isInt(increment) and isInt(upper):
        verifyIncrement(increment)
        printSeq(int(lower),int(increment),int(upper))
    #Floating input
    if isFloat(lower) and isFloat(increment) and isFloat(upper):
        verifyIncrement(increment)
        printSeq(float(lower),float(increment),float(upper))
    #Alpha input
    if len(upper) == 1 and len(lower) == 1 and isInt(increment) and not isInt(upper) and not isInt(lower):
        checkMismatchingBounds(charToInt(lower),charToInt(upper))
        verifyIncrement(int(increment))
        alphaSeq(charToInt(lower),int(increment),charToInt(upper))
    #Roman input
    if romanToInt(lower) != 0  or romanToInt(upper) != 0:
    	computeRoman(lower,increment,upper)
    defaultError('Invalid Input.')
