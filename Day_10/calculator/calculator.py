##################################################################################################

# Created by Sam Insanali
# GitHub: https://github.com/SInsanali

##################################################################################################
# This program is the essential coding project, a calculator

# For this project I am focsing on strengthening my skills with dictionaries, recursion, and functions with outputs. 

# Project outline
#Create functions for each mathematical operator
#Create calculator function
#Create prompt to determine direction of the program

##################################################################################################

from art import logo
from os import system, name

def clear(): 
    """Clears the screen on the console"""
    #for windows
    if name == "nt":
        system("cls")
    #for mac and linux(here, os.name is 'posix')
    else:
        system("clear")

# Input validations functions
def validate_float(prompt_message):
    """Validates user input is a decimal.
    ex. user_input = validate_float("Enter a value: ")"""
    while True:
        input_str = input(prompt_message)
        try:
            return float(input_str)
        except ValueError:
            print("Invalid input. Please enter a valid number")

def validate_operator(prompt_message):
    """Validates user input is a valid operator."""
    valid_inputs = []
    for operator in operations:
        valid_inputs.append(operator)

    while True:
        input_str = input(prompt_message)
        if input_str in valid_inputs:
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
    num1 = validate_float("Enter the first number: ")

    # Print operators
    for operator in operations:
        print(operator)
        run = True # Set var so while loop can execute

    while run:
        chosen_operator = validate_operator("Choose an operator: ")

        num2 = validate_float("Enter the next number: ")

        # Calculator output
        chosen_function = operations[chosen_operator]
        answer = chosen_function(num1, num2)

        # Display output
        print(f"\n{num1} {chosen_operator} {num2} = {answer}")

        # user prompt to continue
        while True:
            valid_options = ["", "n", "x"] #accepted inputs from user
            continue_on = input(f'\nPress "enter" key to continue calculating using {answer}\
                                    \nEnter "n" to start a new calculation\
                                    \nEnter "x" to exit the program\n')
                
            if continue_on in valid_options:
                break
            else:
                print("Choose a valid option")
                

        #program logic
        if continue_on == "":
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
 

