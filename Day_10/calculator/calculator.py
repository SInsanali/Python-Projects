##################################################################################################
# Created by Sam Insanali
# GitHub: https://github.com/SInsanali
##################################################################################################
# This program is the essential coding project, a calculator

# I will be working on improving my skills on functions with outputs

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

# Start program
clear()
print(logo)

run = True
while run:
    # User prompts for first calculation
    num1 = float(input("Enter the first number: "))

    # Print operators
    for operator in operations:
        print(operator)
    
    chosen_operator = input("Choose an operator: ")
    
    num2 = float(input("Enter the second number: "))

    # Calculator output
    chosen_function = operations[chosen_operator]
    initial_answer = chosen_function(num1, num2)

    # Display output
    print(f"\n{num1} {chosen_operator} {num2} = {initial_answer}")

    #NOTE this can be made into a function to code more effiecently 
    calculate_again = input(f'\nEnter "y" to continue calculating using {initial_answer}, or enter "n" to finish calculating: ')

    if calculate_again == "n":
        print("\nThank you for using this program!")
        run = False

    # Second calculation
    # User prompts for next calculation
    chosen_operator = input("\nChoose an operator: ")

    num3 = float(input("Enter the next number: "))

    # Calculator output
    chosen_function = operations[chosen_operator]
    second_answer = chosen_function(initial_answer, num3)

    # Display output
    print(f"\n{initial_answer} {chosen_operator} {num3} = {second_answer}")

    #testing
    break





