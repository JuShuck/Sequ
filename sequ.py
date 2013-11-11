# This program is a modified seq command called sequ. This source code will hose all 5 compliance levels. Compliance level 0 is due on 10/20/2013. Compliance level 1 is due on 11/11/2013
# Name: Justin Shuck
# Copy right (c) Justin Shuck


from sys import argv,exit
import numbers,argparse,sys

#Current version of sequ
__VERSION =  '1.0.0'


#will print the sequence
def printSeq(lower,increment,upper):
    while lower <= upper:
        print(lower)
        lower = lower + increment 

def printf(format,*args):
    sys.stdout.write(format % args)
    print

# Define arguments that are handled in this program
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--version","-v", help="View the current version of sequ", action="count")
group.add_argument("--separator","-s", help="Seperate the sequence by a string", action="count")
group.add_argument("--format","-f", help = "Uses Floating-point Format",action = "count")
group.add_argument("--equalwidth","-w", help = "Equalies the width by adding leading zeros", action = "count")

#Postionals
parser.add_argument("string", nargs="?", default= " ",help = "A string that will seperate the numbers in the sequence")
parser.add_argument("lower", type = int, nargs = "?", help = "Lower bounds of the sequence")
parser.add_argument("upper", type = int, nargs = "?", help = "Upper bounds of the sequence")

args = parser.parse_args()
if args.version == 1:
    print("version"+__VERSION)
    exit(1)
if args.separator == 1:
    print("Separator mode!"+str(argv[2]))
    if len(argv) ==4:
        lower = int(str(argv[2]))
        upper = int(str(argv[3]))
        string = "\n"
    else:
        lower = int(str(argv[3]))
        upper = int(str(argv[4]))
        string = str(argv[2])   
    while lower <= upper:
        print lower,
        print string,
        lower+=1       
    exit(1)
if args.format == 1:
    if len(argv) == 4:
	try:
            lower = int(str(argv[2]))
	    upper = int(str(argv[3]))
        except ValueError:
	    print "Error: Invalid Input"
	    exit(1)
        formatType = "%g"
        while lower <= upper:
	    printf(formatType,lower)
	    lower+=1
	exit(1)
    else:
        lower = int(str(argv[3]))
	upper = int(str(argv[4]))
	formatType = str(argv[2])
    
   #if (id(str(argv[2])) != id("%g")) or (id(str(argv[2])) != id(str("%X"))) or (str(argv[2] !=  "%e") or (str(argv[2]) != "%f")):
	accepted = {'%g','%X','%e','%f'}
	if formatType in accepted:
            while lower <= upper:
                printf(formatType,lower)
                lower+=1
        else:
 	    print 'Error: Invalid format Type'
	    exit(1)	

if args.equalwidth == 1:
    if len(argv) == 4:
         lower = int(str(argv[2]))
	 upper = int(str(argv[3]))
	 increment = 1
	 maxLength = len(argv[3])
    else:
	 lower = int(str(argv[2]))
	 upper = int(str(argv[4]))
	 increment = int(str(argv[3]))
         maxLength = len(argv[4])
    while lower <= upper:
         print str(lower).zfill(maxLength)
	 lower = lower+increment

    exit(1)


# Used to verify that there is not more than 2 arguments(besides the file)
if len(argv) <= 2 or len(argv) > 6:
    print('Error: Invalid number of arguments.')
    exit(1)


#Checks to verify that the arguments are both integers. will terminate with an error if one of the arguments is bad.
if len(argv) >= 3:
    try:
	#castInt()
#cast the arguments to int types
        lower = int(str(argv[1]))
        upper = int(str(argv[2]))
        if len(argv) == 4:
            upper = int(str(argv[3]))
            increment = int(str(argv[2]))
        else:
            increment = 1
    except ValueError:
        print("Error: Invalid argument type")
        exit(1)

    printSeq(lower,increment,upper)
