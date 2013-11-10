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

# Define arguments that are handled in this program
parser = argparse.ArgumentParser()
parser.add_argument("--version","-v", help="View the current version of sequ", action="store_true")
parser.add_argument("--separator","-s", help="Seperate the sequence by a string", action="store_true")
parser.add_argument("--format","-f", help = "Uses Floating-point Format",action = "store_true")
parser.add_argument("--equalwidth","-w", help = "Equalies the width by adding leading zeros", action = "store_true")

#Postionals
parser.add_argument("string", nargs="?", default= " ")
parser.add_argument("lower", type = int, nargs = "?", help = "Lower bounds of the sequence")
parser.add_argument("upper", type = int, nargs = "?", help = "Upper bounds of the sequence")

args = parser.parse_args()
if args.version:
    print("version"+__VERSION)
    exit(1)
if args.separator:
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
if args.format:
    print("Format Mode")
    if len(argv) == 4:
        lower = float(str(argv[2]))
	upper = float(str(argv[3]))
        increment = 1.0
    else:
        lower = float(str(argv[2]))
	upper = float(str(argv[4]))
	increment = float(str(argv[3]))

    printSeq(lower,increment,upper)
    exit(1)
if args.equalwidth:
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
