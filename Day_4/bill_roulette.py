#needs updating to be functional
names = names_string.split(", ")
import random
number_of_candicates = len(names) - 1
random_selection = random.randint(0, number_of_candicates)

print(f"{names[random_selection]} is going to buy the meal today!")