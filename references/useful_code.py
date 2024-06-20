#############################################################################################

# TODO: Indicates a task that needs to be completed.
# NOTE: Provides additional information or context about the code.
# FIXME: Indicates that the code needs to be fixed or requires attention.
# BUG: Marks a known bug that should be fixed.
# HACK: Signals a workaround or a hacky solution that should ideally be improved.
# XXX: Used to draw attention to problematic or confusing code that might need review.


#############################################################################################

#NOTE define clear screen function

from os import system, name

def clear(): 
    """Clears the screen on the console"""
    #for windows
    if name == "nt":
        action = system("cls")
    #for mac and linux(here, os.name is 'posix')
    else:
        action = system("clear")

#############################################################################################

#NOTE Exit program cleanly

#try/ except for clean keyboard interrupt
try:
    #Wrap the main code in here
except KeyboardInterrupt:
    #Print an error message and exit cleanly
    print("\nExecution interrupted by user. Exiting program cleanly.")

#############################################################################################

#NOTE Input validation functions

def validate_integer(input_str):
    """Validates that the input string is an integer."""
    while True:
        try:
            return int(input_str)
        except ValueError:
            input_str = input("Invalid input. Please enter a valid number: ")

def validate_float(input_str):
    """Validates that the input string is a float."""
    while True:
        try:
            return float(input_str)
        except ValueError:
            input_str = input("Invalid input. Please enter a valid number: ")

def validate_non_empty_string(input_str):
    """Validates that the input string is non-empty."""
    while not input_str.strip(): #Remove spaces at the beginning and at the end of the string
        input_str = input("Invalid input. Please enter a non-empty string: ")
    return input_str.strip()

#############################################################################################
