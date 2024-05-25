#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#user input
print("\nWelcome to the PyPassword Generator!\n")
nr_letters = int(input("\nHow many letters would you like in your password?\n"))
nr_symbols = int(input(f"\nHow many symbols would you like?\n"))
nr_numbers = int(input(f"\nHow many numbers would you like?\n"))

#create pw variable to store password
password = ""

#create a for loop to pick random letters, numbers and symbols based on user input
for letter in range(1, nr_letters + 1):
    password += random.choice(letters)

for number in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)

#make password string into a list, shuffle it, and make it a string again
password = list(password)
random.shuffle(password)
password = ''.join(password)

print(f"\nYour password is : {password}")
