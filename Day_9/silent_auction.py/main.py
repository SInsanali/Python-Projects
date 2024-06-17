#Created by Sam Insanali

#Silent auction game
#The focus of this program is to solidify my strengths on working with nested dictionaries

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
print(art.logo)
print("\nWelcome to the Secret Auction")

item_for_sale = input("What are we selling today?\n")

# def user_entry(new_name, new_bid):
#     user_info = {}
#     user_info["bidder_name"] = new_name
#     user_info["bidders_bid"] = new_bid

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

    #TODO  fix this so each user has a new dictionary created for them
    #add info to new dictionary
    user_info = {}
    user_info["name"] = bidders_name
    user_info["bid"] = bid_amount

    all_bidders.append(user_info)

    #continue or break prompt loop
    while True:
        more_bidders = input("\nAre there any other bidders? Type 'y' or 'n'")
        if more_bidders == "y" or more_bidders == "n":
            break
        else:
            print("Please enter a valid single letter (y or n)")

    if more_bidders == "y":
        clear()
    elif more_bidders == "n":
        prompts = False

#testing
print(all_bidders)

#TODO determine the winner