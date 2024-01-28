#!/usr/bin/python3
"""factors.py"""


import sys
import custom_functions
#custom_functions = __import__('custom_functions')

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
            custom_functions.factorize(number)
    file.close()

# Handle file-related errors
except Exception as error:
    if isinstance(error, FileNotFoundError):
        sys.stderr.write(f"Error: {file_path} does not exist\n")
        sys.exit(1)
    elif isinstance(error, IsADirectoryError):
        sys.stderr.write(f"Error: {file_path} is a directory, not a file\n")
        sys.exit(1)
    elif isinstance(error, PermissionError):
        sys.stderr.write(f"Error: Permission denied for file {file_path}\n")
        sys.exit(1)
    elif isinstance(error, IOError):
        sys.stderr.write(f"IOError: {error}\n")
        sys.exit(1)
    elif isinstance(error, OSError):
        sys.stderr.write(f"IOError: {error}\n")
        sys.exit(1)
    # Handle other unknown errors
    else:
        sys.stderr.write(f"An unknown error occured\n")
        sys.exit(1)
