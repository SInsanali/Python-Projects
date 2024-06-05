alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(text, shift):
    encrypted_message = ""
    for char in text:
        #checks if the character is a letter in list "alphabet"
        if char in alphabet:

            #find index number for the character
            char_og_position = alphabet.index(char)

            #add the shift while the character is represented as an index value
            char_new_position = char_og_position + shift

            #convert back to a letter
            new_char = alphabet[char_new_position]

            #append to string
            encrypted_message += new_char


        #if not in alphabet, append to string 
        else:
            encrypted_message += char
            
    #print output
    print(f"The encoded text is: {encrypted_message}")

encrypt(text, shift)

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 