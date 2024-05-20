# Greeting message
print("Welcome to the tip calculator.\n")

# Ask for the total bill and make it a float
bill_amount = float(input("What is the total amount of the bill?\n$"))

# Ask for the percentage of the tip and make it a float
tip_percentage = float(
    input("\nWhat percentage of tip would you like to give? \n"))

# Ask for the number of people to split the bill with
people_paying = int(input("\nHow many people will be splitting the bill?\n"))

# Incorperate the tip percentage into the bill amount
tip_as_decimal = tip_percentage / 100
tip_amount = bill_amount * tip_as_decimal
bill_plus_tip = bill_amount * (1 + tip_as_decimal)

# Divide the bill plus tip by the number of people paying
amount_per_person = bill_plus_tip / people_paying

# Deliver the bad news
print(f"\nThe tip amount is ${tip_amount:.2f}")
print(f"The total bill plus tip is ${bill_plus_tip:.2f}")
print(f"Each person should pay ${amount_per_person:.2f}")
