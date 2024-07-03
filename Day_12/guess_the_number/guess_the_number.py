##################################################################################################
# Created by Sam Insanali
# GitHub: https://github.com/SInsanali
##################################################################################################
# Description:
#This program is a pretty fun guessing game, give it a try!
#The goal is to practice defining the scope of the code that I write
#emphasis on using/modifying global and local variables.

#I could do what I usually do and add input validation for everything
##################################################################################################
from art import logo
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

def decrease_lives():
    global player_lives
    return player_lives - 1

def player_hint():
    global RANDOM_NUMBER, guess
    if guess > RANDOM_NUMBER:
        print("[-] Too high")
    else:
        print("[-] Too low")


#####program#####
try:   
    clear()
    print(logo)

    RANDOM_NUMBER = random.randint(1,100) #random number picked from computer #this is a global constant

    print("[-] I'm thinking of a number between 1 and 100")
    game_difficulty = input('[?] Choose a difficulty, type "easy" or "hard" : ') # i'll add input validation later if i feel like it. 

    #set player lives based on the difficulty chosen
    if game_difficulty == "easy":
        player_lives = 10
    elif game_difficulty == "hard":
        player_lives = 5


    print(RANDOM_NUMBER) #testing

    while player_lives != 0:
        print(f"[-] You have {player_lives} guesses left")
        guess = int(input("\n[?] Guess a number: "))

        if guess == RANDOM_NUMBER:
            print(f"[-] You got it! The answer was {RANDOM_NUMBER}")
            break
        else: 
            player_lives = decrease_lives()
            player_hint()
            
    if player_lives == 0:
        print(f"[-] You ran out of guesses, the answer was {RANDOM_NUMBER}")
        
except KeyboardInterrupt:
    print("\nExecution interrupted by user. Exiting program.")