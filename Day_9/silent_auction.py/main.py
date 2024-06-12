#Created by Sam Insanali

#Silent auction game
#The focus of this program is to solidify my strengths on working with nested dictionaries

from os import system, name

# define clear screen function
def clear():
 
    # for windows
    if name == "nt":
        action = system("cls")
 
    # for mac and linux(here, os.name is 'posix')
    else:
        action = system("clear")
