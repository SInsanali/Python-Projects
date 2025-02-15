##################################################################################################
##################################################################################################
# Created by Sam Insanali
# GitHub: https://github.com/SInsanali
##################################################################################################
##################################################################################################
# Description:
# This program simulates a coffe machine, it is part of the 100 days of code challenge.
##################################################################################################
##################################################################################################

from recipies import machine_input

#clear screen function
from os import system, name
def clear(): 
    """Clears the screen on the console"""
    #for windows
    if name == "nt":
        system("cls")
    #for mac and linux(here, os.name is 'posix')
    else:
        system("clear")

# print(machine_input[1])

clear()
print(f"What would you like? (espresso/latte/cappuccino):")

