##################################################################################################
# Created by Sam Insanali
# GitHub: https://github.com/SInsanali
##################################################################################################
# This program is the essential coding project, a calculator

# For this project I am focsing on strengthening my skills with dictionaries, recursion, and functions with outputs. 

# Project outline
#Create functions for each mathematical operator
#Create calculator function
#Create prompt to determin direction of the program

##################################################################################################

from art import logo
from os import system, name

def clear(): 
    """Clears the screen on the console"""
    #for windows
    if name == "nt":
        action = system("cls")
    #for mac and linux(here, os.name is 'posix')
    else:
        action = system("clear")

#BUG
# Input validations functions
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

def validate_operator(input_str):
    """Validates that the input is in operations"""
    while True:
        for symbol in operations:
            if input_str == symbol:
                return input_str
            else:
                print("Please choose a valid operator")



# Functions for various operators
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2

# Dictionary with all functions
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "^" : exponent,
}


def calculator():
    # User prompts for first calculation
    num1 = validate_float(float(input("Enter the first number: "))) #XXX

    # Print operators
    for operator in operations:
        print(operator)
        run = True # Set var so while loop can execute

    while run:
        chosen_operator = validate_operator(input("Choose an operator: ")) #XXX

        num2 = validate_float(float(input("Enter the next number: "))) #XXX

        # Calculator output
        chosen_function = operations[chosen_operator]
        answer = chosen_function(num1, num2)

        # Display output
        print(f"\n{num1} {chosen_operator} {num2} = {answer}")

        # user prompt to continue
        continue_on = input(f'\nPress "enter" key to continue calculating using {answer}\
                                \nEnter "n" to start a new calculation\
                                \nEnter "x" to exit the program\n')

        if continue_on == "y":
            num1 = answer
        elif continue_on == "n":
            calculator() #recursion used here
        elif continue_on == "x":
            print("\nThank you for using this program!")
            run = False


# Start program
try:
    clear() # Clear console 
    print(logo) 
    calculator() 

except KeyboardInterrupt:
    #Print an error message and exit cleanly
    print("\nExecution interrupted by user. Exiting program.")

#TODO add input validation to user inputs. 
