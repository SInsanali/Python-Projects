##################################################################################################
##################################################################################################
# Created by Sam Insanali
# GitHub: https://github.com/SInsanali
##################################################################################################
##################################################################################################
# Description:
# This script [provide a brief description of what your script does].

# Example: 
# This script analyzes network traffic to identify potential security threats using 
# machine learning algorithms. 
##################################################################################################
##################################################################################################
import art
from game_data import data as names
import random

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

#pick random name from game_data
def pick_random_name():
    first_choice = random.choice(names)
    print(first_choice("name:"))


#pick second random name from game_data


clear()
print(art.logo)
pick_random_name()
