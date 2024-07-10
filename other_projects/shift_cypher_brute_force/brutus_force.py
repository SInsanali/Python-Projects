##################################################################################################
# Created by Sam Insanali
# GitHub: https://github.com/SInsanali
##################################################################################################
# Description:
# This script will use a brute force method to decypher a shift cypher.
##################################################################################################
from art import banner

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shift_counter = 1 #used to determine the shift value

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

def cypher_crack():
    output_text = ""
    global shift_counter

    for char in user_input:
        if char in ALPHABET: #check is character is a letter
            #find index number for the character
            og_char_position = ALPHABET.index(char)
            #shift the index
            new_char_position = (og_char_position + shift_counter) % 26 
            #add new char to output string
            new_char = ALPHABET[new_char_position]
            output_text += new_char
        
        else: #if not a letter, add on the output string
            output_text += char

    print(f"\n[{shift_counter}] {output_text}")
    
    #increase shift_counter increment by 1
    shift_counter += 1

            
try:
    clear()
    print(banner)
    user_input = input("[?] Enter the cypher text to be cracked:\n").lower()

    print("\n[+] All possible outputs:")
    while shift_counter < 26:
        cypher_crack()

except KeyboardInterrupt:
   print("\nExecution interrupted by user. Exiting program.")

