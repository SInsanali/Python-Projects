##################################################################################################
##################################################################################################
# Created by Sam Insanali
# GitHub: https://github.com/SInsanali
##################################################################################################
##################################################################################################
# Description:
# This script helps to calculate the fees related to using PayPal Goods & Services.
##################################################################################################
##################################################################################################

# clear screen function
from os import system, name

def clear(): 
    """Clears the screen on the console"""
    # for Windows
    if name == "nt":
        system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        system("clear")

# art
logo = """
    ____              ____        __   ______                __        ___        _____                 _                   ______             ______      __           __      __            
   / __ \____ ___  __/ __ \____ _/ /  / ____/___  ____  ____/ /____   ( _ )      / ___/___  ______   __(_)_______  _____   / ____/__  ___     / ____/___ _/ /______  __/ /___ _/ /_____  _____
  / /_/ / __ `/ / / / /_/ / __ `/ /  / / __/ __ \/ __ \/ __  / ___/  / __ \/|    \__ \/ _ \/ ___/ | / / / ___/ _ \/ ___/  / /_  / _ \/ _ \   / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
 / ____/ /_/ / /_/ / ____/ /_/ / /  / /_/ / /_/ / /_/ / /_/ (__  )  / /_/  <    ___/ /  __/ /   | |/ / / /__/  __(__  )  / __/ /  __/  __/  / /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
/_/    \__,_/\__, /_/    \__,_/_/   \____/\____/\____/\__,_/____/   \____/\/   /____/\___/_/    |___/_/\___/\___/____/  /_/    \___/\___/   \____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     
            /____/                                                                                                                                                                            """


# PayPal fees
fixed_fee = 0.49
fixed_rate = 0.0349

# Validate user input as a decimal
def validate_float(prompt_message):
    """Validates user input is a decimal."""
    while True:
        input_str = input(prompt_message)
        try:
            return float(input_str)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Calculate net amount when receiving money
def calculate_paypal_fee(amount):
    """Calculates PayPal fee and net amount received for a given input amount."""
    paypal_fee = (amount * fixed_rate) + fixed_fee
    net_amount = amount - paypal_fee
    return paypal_fee, net_amount

# Calculate amount to request to receive a target amount after fees
def calculate_amount_for_target_net(target_net):
    """Calculates the amount to ask for to receive a target net amount after PayPal fees."""
    amount = (target_net + fixed_fee) / (1 - fixed_rate)
    paypal_fee = amount - target_net
    return amount, paypal_fee


# Operation of the script
try:
    program_running = True

    while program_running:
        # Clear screen
        clear()

        print(logo)
        print(f"\nWelcome to the PayPal Goods & Services Fee Calculator!")
        print("\nCreated by Sam Insanali || GitHub: https://github.com/SInsanali ")

        # Input from user with validation
        amount = validate_float(f"\n[!] Enter an amount: $")

        # Calculate net received and PayPal fee for the input amount
        paypal_fee, net_received = calculate_paypal_fee(amount)

        print(f"\n[-] If you ask for ${amount:.2f}, you'll receive ${net_received:.2f} after PayPal takes ${paypal_fee:.2f}.")

        # Calculate amount needed to receive the specified input amount after fees
        ask_for, paypal_fee_for_target = calculate_amount_for_target_net(amount)

        print(f"\n[-] If you want to receive ${amount:.2f} after fees, you should ask for ${ask_for:.2f}, PayPal will take ${paypal_fee_for_target:.2f}.\n")

        # Ask if the user wants to perform another calculation
        while True:
            play_again = input("\n[?] Would you like to calculate again? (Y/n): ").strip().lower()
            if play_again in ["y", "n", ""]:
                break
            else:
                print("[!] Please enter 'Y' to continue or 'n' to exit.")

        # Run program again logic
        if play_again == "y" or play_again == "":
            continue  # restart the loop for another calculation
        else:
            print("[-] Thank you for using the PayPal Goods & Services Fee Calculator!")
            program_running = False  # exit the loop and end the program

except KeyboardInterrupt:
    # Print an error message and exit cleanly
    print("\nExecution interrupted by user. Exiting program.")
