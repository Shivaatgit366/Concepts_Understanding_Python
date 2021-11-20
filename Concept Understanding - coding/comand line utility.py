# Command line utility helps to run the Python program in other languages which uses console/command prompts.
# this below Python program we want to run in windows powershell. So we create a command line utility.
# the modules argparse and sys helps us to create command line utility in Python.

import argparse
import sys

def calc(args):  # a simple addition function is defined in the end.
    if args.o == "add":
        return args.x + args.y

    elif args.o == "sub":
        return args.x - args.y

    elif args.o == "mul":
        return args.x * args.y

    elif args.o == "div":
        return args.x / args.y

    else:
        return "something went wrong"

if __name__ == '__main__':

    parser = argparse.ArgumentParser()  # an object "parser" is being created using the class "ArgumentParser"
    parser.add_argument("--x", type=float,
                        default=1.0,
                        help="Enter first number. This is a utility for calculating numbers. Plz contact Shiva")
# add_argument function is used with so many arguments. Here x is the number used.
    parser.add_argument("--y", type=float,
                        default=3.0,
                        help="Enter second number. This is a utility for calculating numbers. Plz contact Shiva")
# add_argument function is used with so many arguments. Here y is the number used.
    parser.add_argument("--o", type=str, default="add",
                        help="This is a utility for calculating numbers. Plz contact Shiva for more")
# add_argument function is used with so many arguments. This is just a general statement. It is a string.

# now, we use parse_args function for parsing the argument which we have created above.
    args = parser.parse_args()
# now, using sys module, we use stdout function and write function which takes string of "args" calculation.
    sys.stdout.write(str(calc(args)))  # write function just writes the function on console screen.

# so this program can be used for mathematical operations in console.

# --------------------------------*------------------------*---------------------*------------------------*--------

