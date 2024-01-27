#!/usr/bin/python3
"""factors.py"""


import sys

custom_functions = __import__('custom_functions')

# Check if the correct number of command-line arguments is provided
argument_counter = len(sys.argv)
if argument_counter != 2:
    sys.stderr.write(f"Usage: factors <file>\n")
    sys.exit(1)

# Extract the file path from command-line arguments
file_path = sys.argv[1]
try:
    with open(file_path, "r") as file:
        for line in file:
            number = int(line)
            if number == 1:
                print(f"{number}=1*1")
                continue
            if number == 0:
                print(f"{number}=0*0")
                continue
            # Call the function to print factors of the number
            custom_functions.print_factors(number)

# Handle file-related errors
except (FileNotFoundError, FileExistsError):
    sys.stderr.write(f"{file_path} does not exist\n")
    sys.exit(1)

# Handle other unknown errors
except Exception as error:
    sys.stderr.write(f"An unknown error occured\n")
    sys.exit(1)
