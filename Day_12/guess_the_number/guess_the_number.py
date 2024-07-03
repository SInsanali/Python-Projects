##################################################################################################
# Created by Sam Insanali
# GitHub: https://github.com/SInsanali
##################################################################################################
# Description:
#This program is a pretty fun guessing game, give it a try!
#The goal is to practice defining the scope of the code that I write
#emphasis on using/modifying global and local variables.

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

def validate_integer(prompt_message):
    """Validates user input is an integer.
    ex. user_input = validate_integer("Enter a value: ")"""
    while True:
        input_str = input(prompt_message)
        try:
            return int(input_str)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

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
    program_running = True

    while program_running:
        clear()
        print(logo)

        RANDOM_NUMBER = random.randint(1,100) #random number picked from computer #this is a global constant

        print("[-] I'm thinking of a number between 1 and 100")

        while True:
            game_difficulty = input('[?] Choose a difficulty, type "easy" or "hard" : ').lower()
            valid_options = ["easy", "hard"]
            if game_difficulty in valid_options:
                break
            else:
                print("[!] Please enter a valid input.")
            
        #set player lives based on the difficulty chosen
        if game_difficulty == "easy":
            player_lives = 10
        elif game_difficulty == "hard":
            player_lives = 5

        while player_lives != 0:
            print(f"[-] You have {player_lives} guesses left")

            #check if the number is between 1 and 100
            #bart proof
            while True:
                guess = validate_integer("\n[?] Guess a number: ")
            
                if 0 < guess < 100:
                    break
                else:
                    print("[!] Pick a number between 1 and 100.")

            if guess == RANDOM_NUMBER:
                print(f"[-] You got it! The answer was {RANDOM_NUMBER}")
                break
            else: 
                player_lives = decrease_lives()
                player_hint()
                
        if player_lives == 0:
            print(f"[-] You ran out of guesses, the answer was {RANDOM_NUMBER}")
            
        
            #run program again? 
        while True:
            valid_input = ["1", "2"]
            play_again = input("\n[?] Type '1' to play again | Type '2' to end the program: ")

            if play_again in valid_input:
                break
            else:
                print("[!] Please choose a valid option")


            #run program again logic
        if play_again == "1":
            continue #restart the loop for another conversion
        else:
            print("[-] Thank you for using this program")
            program_running = False #exit the loop and end the program

except KeyboardInterrupt:
    print("\nExecution interrupted by user. Exiting program.")