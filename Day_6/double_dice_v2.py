import random

# Create dice faces
dice_faces = [
    '''
    -----
    |   |
    | o |
    |   |
    -----
    ''',
    '''
    -----
    |o  |
    |   |
    |  o|
    -----
    ''',
    '''
    -----
    |o  |
    | o |
    |  o|
    -----
    ''',
    '''
    -----
    |o o|
    |   |
    |o o|
    -----
    ''',
    '''
    -----
    |o o|
    | o |
    |o o|
    -----
    ''',
    '''
    -----
    |o o|
    |o o|
    |o o|
    -----
    '''
]

# Function to roll a die
def roll_die():
    random_index = random.randint(0, 5)
    return dice_faces[random_index], random_index + 1

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
