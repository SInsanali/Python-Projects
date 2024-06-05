import art

# Tons of pseudo code in this to help me understand the logic as I code :)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Define functions
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

# Need to update this to made the program a while loop so it can handle input errors and continue on. 

print(art.banner)

run = True

while run:
    # Gather user inputs and output conditional logic
    direction = input('\nType "e" to encode, type "d" to decode:\n')
    #input validation
    if direction != "e" and direction != "d":
        print("Please enter a valid single letter.")
        continue

    text = input("Enter your message to be converted:\n").lower()
    
    shift_input = input("How many places will this be shifted?:\n")
    # Input validation for shift
    
    
    #need to work on this
    if not shift_input.isdigit():
        print("Please enter a valid number.")
        continue
    shift = int(shift_input)
    #need to work on this
    


    #execute logic
    logic(direction, text, shift)

    #run or end program
    go_again = input('\nWould you like to run the program again? Type "y" to run again or "n" to end the program:\n')

    # Asks the user if they want to go again and adds input validation.
    if go_again != "y" and go_again != "n":
        print("Please enter a valid single letter.")
        continue
    elif go_again == "y":
        continue
    elif go_again == "n":
        run = False
        print("Thank you for using this program!")
