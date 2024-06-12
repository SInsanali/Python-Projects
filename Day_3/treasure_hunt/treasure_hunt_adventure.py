## Treasure Island Adventure Game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your objective is to find the treasure.\n") 

# First choice
first_choice = input("\nYou arrive at a fork in the road. Where do you go? Type 'left' or 'right'\n").lower()

if first_choice == "left":
    # Advance to second choice
    second_choice = input("\nYou arrive at a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()

    if second_choice == "wait":
        # Advance to third choice
        third_choice = input("\nYou arrive at the island unharmed and see a house with 3 doors.\nType 'red' to enter the red door. Type 'yellow' to enter the yellow door. Type 'blue' to enter the blue door.\n").lower()

        if third_choice == "yellow":
            print("\nCongratulations! You found the treasure, you're rich!")
        elif third_choice == "red":
            print("\nYou enter a room full of fire and are burned. Game over!")
        elif third_choice == "blue":
            print("\nYou enter a room full of beasts and are eaten. Game over!")
        else:
            print("\nYou chose a door that doesn't exist. Game over!")
    else:
        print("\nYou are surrounded by sharks and eaten. Game over!")

elif first_choice == "right":
    print("\nYou stepped on a land mine and were blew up! Game over!")
else:
    print("\nYou picked a wrong direction and were vaporized. Game over!")
