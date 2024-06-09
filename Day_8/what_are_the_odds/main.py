import random
import time


print("\nWhat are the odds?\n")

number_range = input("Determine the acceptable range: \n1 - ")
if not number_range.isdigit():
    print("Please enter a valid number")
else:
    number_range = int(number_range)

user_guess = input(f"Guess a number from 1 to {number_range}: \n")
if not user_guess.isdigit():
    print("Please enter a valid number")
else:
    user_guess = int(user_guess)

computer_guess = random.randint(1, number_range)

def countdown(time_in_seconds):
    print(f"\nCounting down from {time_in_seconds}")
    for seconds in range(time_in_seconds, 0, -1):
        print(f"{seconds}...")
        time.sleep(1)

countdown(3)
print(f"\nYour guess was {user_guess}.")
print(f"My guess was {computer_guess}.")
if computer_guess == user_guess:
    print("\nLooks like I got you, sucker!")
else:
    print("\nYou win... for now.")