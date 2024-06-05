# Tons of pseudo code in this to help me understand the logic as I code :)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Gather user inputs
direction = input('Type "e" to encode, type "d" to decode:\n')
text = input("Enter your message to be converted:\n").lower()
shift = int(input("How many places will this be shifted?:\n"))

# Define functions
def encode(plain_text, shift_value):
    cypher_text = ""
    for char in plain_text:
        # Checks if the character is a letter in list "alphabet"
        if char in alphabet:
            # Find index number for the character
            char_og_position = alphabet.index(char)
            # Add the shift while the character is represented as an index value
            char_new_position = (char_og_position + shift_value) % 26
            # Convert back to a letter
            new_char = alphabet[char_new_position]
            # Append to string
            cypher_text += new_char
        # If not in alphabet, append to string 
        else:
            cypher_text += char
    
    # Print output
    print(f"The encoded text is: {cypher_text}")

def decode(encoded_text, shift_value):
    decoded_text = ""
    for char in encoded_text:
        if char in alphabet:
            char_og_position = alphabet.index(char)
            char_new_position = (char_og_position - shift_value) % 26
            new_char = alphabet[char_new_position]
            decoded_text += new_char
        else:
            decoded_text += char
            
    print(f"The decoded text is: {decoded_text}")

# Output conditional logic
if direction == "e":
    encode(text, shift)
elif direction == "d":
    decode(text, shift)
else:
    print("Please choose a valid entry")
