import random

#create dice faces
one = '''
-----
|   |
| o |
|   |
-----
'''

two = '''
-----
|o  |
|   |
|  o|
-----
'''

three = '''
-----
|o  |
| o |
|  o|
-----
'''

four = '''
-----
|o o|
|   |
|o o|
-----
'''

five = '''
-----
|o o|
| o |
|o o|
-----
'''

six = '''
-----
|o o|
|o o|
|o o|
-----
'''

#make list with all dice faces
dice_faces = [one, two, three, four, five, six]

#welcome message to the user
print("\nForget to bring your dice? Here's a roll on the house\n")

#Generate two random numbers 
random_number_1 = random.randint(0,5)
random_number_2 = random.randint(0,5)

#randomly select dice faces
dice_face_chosen_1 = dice_faces[random_number_1]
dice_face_chosen_2 = dice_faces[random_number_2]

#calculate value for each dice face chosen
dice_value_1 = random_number_1 + 1
dice_value_2 = random_number_2 + 1

#calculate total value of the roll
total_dice_value = dice_value_1 + dice_value_2

# print die faces and total value
print(dice_face_chosen_1 + dice_face_chosen_2) 
print(f"The total value of your roll is: {total_dice_value}")

