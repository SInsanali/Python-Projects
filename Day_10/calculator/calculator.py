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
#NOTE do the brackets need to be there?
opertaions = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "^" : exponent,
}

# Start program
clear()
print(logo)

# User prompts
num1 = float(input("Enter the first number: "))

for operator in opertaions:
    print(operator)

chosen_operator = input("Choose an operator: ")

num2 = float(input("Enter the second number: "))


# Calculator output
chosen_function = opertaions[chosen_operator]
answer = chosen_function(num1, num2)

print(f"\n{num1} {chosen_operator} {num2} = {answer}")
