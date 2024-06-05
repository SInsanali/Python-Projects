#create rock, paper, and scissors variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#import modules
import random

#welcome message and get user input
print("\nWelcome to Rock, Paper, Scissors! Can you beat the computer?")

#make user choice and generate random number for computer choice
user_choice = int(input("Which do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
computer_choice = random.randint(0,2)

#create list of options
options = [rock, paper, scissors]
choices = [user_choice, computer_choice]
valid_inputs = [0, 1, 2]

#print users choice with user input as the index and print computers choice with random number as the index
#add input validation
if user_choice not in valid_inputs:
   print("\nYou entered an invalid choice, you lose!")

else:
    print(f"\nYou chose: \n{options[user_choice]}")
    print(f"\nThe computer chose: \n{options[computer_choice]}")


#create conditional statements to determine who wins
if choices == [0,2] or choices == [1,0] or choices == [2,1]:
  print("\nYou win!")
    
elif choices == [0,0] or choices == [1,1] or choices == [2,2]:
    print("\nIt's a draw!")
    
else:
    print("\nThe computer wins!")

