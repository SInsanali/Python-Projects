import random
from art import dice_faces

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

# Function to roll a die
def roll_die():
    random_index = random.randint(0, 5)
    return dice_faces[random_index], random_index + 1

try:

    continue_on = True

    while continue_on:
        clear()

        # Welcome message to the user
        print("\nForget to bring your dice? Here's a roll on the house\n")

        # Roll two dice
        dice_face_1, dice_value_1 = roll_die()
        dice_face_2, dice_value_2 = roll_die()

        # Calculate total value of the roll
        total_value = dice_value_1 + dice_value_2

        # Print the results
        print(dice_face_1 + dice_face_2)
        print(f"The total value of your roll is: {total_value}")

        while True:
            roll_again = input('Press "enter" to roll again\
                                \nPress "x" to exit the program\n') 

            if roll_again == "":
                break
            elif roll_again == "x":
                print("Thanks for using this program!")
                continue_on = False
                break
            else:
                print("Invalid input, try again.")

except KeyboardInterrupt:
    print("\nExecution interrupted by user. Exiting program.")
