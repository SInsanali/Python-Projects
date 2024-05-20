#Introduction to program
print("This program will tell you if a year is a leap year.")

# Ask question: Which year do you want to check?
year = int(input("\nWhich year do you want to check?\n"))

#The following diectates a leap year:
# - every year that is divisible by 4 with no remainder
# - except every year that is evenly divisible by 100 with no remainder
# - unless the year is also divisible by 400 with no remainder
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"\n{year} is a leap year")
    else:
      print(f"\n{year} is not a leap year")
  else:
    print(f"\n{year} is a leap year")
else:
  print(f"\n{year} is not a leap year")
