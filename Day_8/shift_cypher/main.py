#!/usr/bin/python
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Define function
def logic(instruction, input_text, shift_value):
    output_text = ""
   
    # Used for later functionality in a print statement
    if instruction == "e":
        operation = "encoded"
    elif instruction == "d":
        operation = "decoded"

    for char in input_text:
        # Checks if the character is a letter in list "alphabet"
        if char in alphabet:
            # Find index number for the character
            char_og_position = alphabet.index(char)
            # Add or subtract the shift value while the character is represented as an index value
            if instruction == "e":
                char_new_position = (char_og_position + shift_value) % 26
            elif instruction == "d":
                char_new_position = (char_og_position - shift_value) % 26
            # Convert back to a letter        
            new_char = alphabet[char_new_position]
            # Append to string
            output_text += new_char
        # If not in alphabet, append to string
        else:
            output_text += char
            
    print(f"\nYour {operation} text is: {output_text}") 


print(art.banner[2])

run = True

while run:
    # Gather user inputs and output conditional logic
    direction = input('\nType "e" to encode, type "d" to decode:\n')
    #input validation
    if direction != "e" and direction != "d":
        print("\nPlease enter a valid single letter (e or d).")
        continue

    text = input("Enter your message to be converted:\n").lower()
    
    while True:
        shift_input = input("How many places will this be shifted?:\n")   

        if shift_input.isdigit():
            shift = int(shift_input)
            break
        else:
            print("\nPlease enter a valid number.")

    #call logic function
    logic(direction, text, shift)

    #run or end program
    while True:
        go_again = input('\nWould you like to run the program again? Type "y" to run again or "n" to end the program:\n')
        if go_again == "y" or go_again == "n":
            break

        else:
            print("\nPlease enter a valid single letter (y or n).\n")
    
    if go_again == "n":
        run = False
        print("\nThank you for using this program!")
