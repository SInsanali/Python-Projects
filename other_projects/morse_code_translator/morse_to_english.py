##################################################################################################
# Morse Code Translator
##################################################################################################
# Created by Sam Insanali
# GitHub: https://github.com/SInsanali
##################################################################################################
# Description:
# This script converts text to Morse code and vice versa using dictionaries.
#
# This script allows users to enter a text message and converts it into Morse code,
# or input Morse code and translates it back into the corresponding text.
##################################################################################################

import conversion_guide
from art import logo

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

# def program_instructions():
#     instuctions = input('Press "Enter" ')


def english_to_morse(provided_input):
    """converts english text to morse code"""
    morse_output = ""
    
    for char in provided_input:
        if char in conversion_guide.english_to_morse:
            char = conversion_guide.english_to_morse[char]
            morse_output += char + " "
        else:
            morse_output += char + " " #if character is not found, keep it as is

    morse_output = morse_output.strip() #removes any white spaces from the beginning and end
    print(f'\n[-] User input: "{user_input}"\n[-] Morse Code output: {morse_output}')


def morse_to_english(provided_input):
    """converts morse code to english text"""
    letters = provided_input.split(" ")
    english_output = ""
    
    for letter in letters:
        if letter in conversion_guide.morse_to_english:
            english_char = conversion_guide.morse_to_english[letter]
            english_output += english_char
        else:
            english_output += letter #if character is not found, keep it as is
    
    english_output = english_output.strip() #removes any white spaces from the beginning and end
    print(f'\n[-] User input: "{user_input}"\n[-] English output: "{english_output.upper()}"')





#########################
######## program ########
#########################
try:
    clear()
    print(logo)
    run_program = True
    while run_program:
        print("\n[-] Option 1: Translate English text to Morse Code")
        print("[-] Option 2: Translate Morse Code to English text")

        while True:
            valid_input = ["1", "2"]
            program_purpose = input("\n[?] Type '1' for Option 1 or '2' for Option 2: ")

            if program_purpose in valid_input:
                break
            else:
                print("[!] Please choose a valid option")


        user_input = input("[?] Enter the message to be converted: ").lower().strip()

        if program_purpose == "1":
            english_to_morse(user_input)
        elif program_purpose == "2":
            morse_to_english(user_input)

        #run program again? 
        while True:
            valid_input = ["1", "2"]
            convert_again = input("\n[?] Type '1' to perform another conversion | Type '2' to end the program: ")

            if convert_again in valid_input:
                break
            else:
                print("[!] Please choose a valid option")

        #run program again logic
        if convert_again == "1":
            continue #restart the loop for another conversio
        else:
            print("[-] Thank you for using this program")
            run_program = False #exit the loop and end the program

except KeyboardInterrupt:
    print("\n[!] User keyboard interrupt, exiting program.")
