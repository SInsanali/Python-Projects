##################################################################################################
# Created by Sam Insanali
# GitHub: https://github.com/SInsanali
##################################################################################################
# Description:
# Silent auction game
#T he focus of this program is to solidify my strengths on working with nested dictionaries
##################################################################################################


from os import system, name
import art

#define clear screen function
def clear(): 
    #for windows
    if name == "nt":
        action = system("cls")
    #for mac and linux(here, os.name is 'posix')
    else:
        action = system("clear")

#program start banner
clear()

print(art.logo)
print("\nWelcome to the Secret Auction")
item_for_sale = input("What are we selling today?\n")

#loop to prompt and handle user inputs
all_bidders = []
prompts = True
while prompts:
    #get bidders name
    bidders_name = input("What is your name?\n")
    if not bidders_name.isalpha():
        print("Please enter a valid name")
        continue
    
    #get bid amount
    while True:
        bid_amount = input("How much would you like to bid?:\n$")
        if bid_amount.isdigit():
            bid_amount = int(bid_amount)
            break
        else:
            print("\nPlease enter a valid number")

    #add info to new dictionary
    user_info = {}
    user_info["name"] = bidders_name
    user_info["bid"] = bid_amount

    all_bidders.append(user_info)

    #continue or break prompt loop
    while True:
        more_bidders = input("\nAre there any other bidders? Type 'y' or 'n'\n")
        if more_bidders == "y" or more_bidders == "n":
            break
        else:
            print("Please enter a valid single letter (y or n)")

    if more_bidders == "y":
        clear()
    elif more_bidders == "n":
        prompts = False 


#determine the winner
winner = ""
highest_bid = 0

for bidder in all_bidders:
    if bidder["bid"] > highest_bid:
        highest_bid = bidder["bid"]
        winner = bidder["name"]

        #In the auction the first person to make a bid for the highest amount will win the auction
        #unless someone else beats that bid. 
        
    
print(f"\nThe winner is {winner}, with a bid of ${highest_bid} for {item_for_sale}.")

