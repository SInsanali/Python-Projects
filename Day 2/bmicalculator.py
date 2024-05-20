# Welcome message
print("Welcome to the BMI calculator\n")

# Get the users height
print("Let's start off with getting your height")
height = float(input("What is your height in inches?\n"))

# Get the users weight
print("\nOkay great, now lets get your weight")
weight = float(input("What is your weight in lbs?\n"))

# Plug inputs into BMI formula
#bmi = (weight in lbs / (height in inches^2)) * 703
bmi = (weight / (height ** 2)) * 703

#Dictate health classes based on BMI and deliver the news
if bmi < 18.5:
  print(f"\nYour BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"\nYour BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"\nYour BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"\nYour BMI is {bmi}, you are obese.")
else:
  print(f"\nYour BMI is {bmi}, you are clinically obese.")
