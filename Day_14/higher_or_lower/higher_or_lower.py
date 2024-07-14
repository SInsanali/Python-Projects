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
from game_data import data
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
    random_name = random.choice(data)
    return random_name
    
try:

    clear()
    print(art.logo)
    user_score = 0
    program_running = True

    #display first choice to user
    choice_a = pick_random_name()

    #while loop starts here
    while program_running:
        print(f"\n[+] Option A: {choice_a["name"]}, a {choice_a["description"]}, from {choice_a['country']}")

        #ensure b != a
        while True:
            choice_b = pick_random_name()
            if choice_b!= choice_a:
                break
            else:
                continue

        #print vs logo
        print(art.vs)

        #display second choice to user
        print(f"\n[+] Option B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")

        #determine who has more IG followers
        correct_answer = ""

        if choice_a["follower_count"] > choice_b["follower_count"]:
            correct_answer = "A"
        elif choice_a["follower_count"] < choice_b["follower_count"]:
            correct_answer = "B"

        #make compare choice_a and choice_b
        while True:
            valid_inputs = ["A", "B"]
            user_choice = input("\n[?] Who has more followers on Instagram? (A/B): ").upper()

            if user_choice in valid_inputs:
                break
            else:
                print("\n[!] Invalid input. Please enter either 'A' or 'B'.")

        if user_choice == correct_answer:
            user_score += 1
            choice_a = choice_b
            clear()
            print(art.logo)
            print(f"\n[*] Correct! Your current score is: {user_score}")
        elif user_choice!= correct_answer:
            print(f"\n[-] Game over! The correct answer was {correct_answer}. Your final score is: {user_score}")
            program_running = False

except KeyboardInterrupt:
    print("\nExecution interrupted by user. Exiting program.")