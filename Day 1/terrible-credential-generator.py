# Make an introduction message
print(
    "Welcome to the terrible credential generator\n\n"
    "I just need a few pieces of information to make terrible credentials for you\n"
)

#  Define variables
first_name = input("\nWhat is your first name?\n")
last_name = input("\nWhat is your last name?\n")
ssn = input("\nWhat is your social security number?\n")
pet_name = input("\nWhat is your pet's name?\n")
birth_year = input("\nWhat year were you born?\n")

# Deliver the terrible credential
print("\nHere are your terrible credentials:")
print("\nYour username is:" + first_name + last_name + ssn)
print("\nYour password is:" + pet_name + birth_year)