##################################################################################################
# Created by Sam Insanali
# GitHub: https://github.com/SInsanali
##################################################################################################
# Description:
# This program is an interactive blackjack game
# The goal is to test all of the skills I've leaned up to this point.
##################################################################################################
from art import banner
import random

#cards in deck and players hands
deck = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players_cards = []
dealers_cards = []

#clear screen function
from os import system, name
def clear(): 
    """Clears the screen on the console"""
    #for windows
    if name == "nt":
        system("cls")
    #for mac and linux(here, os.name is 'posix')
    else:
        system("clear")


def deal_a_card(): 
    random_card_choice = random.choice(deck)
    players_cards.append(random_card_choice)
       
    random_card_choice = random.choice(deck)
    dealers_cards.append(random_card_choice)

def calculate_player_score():
    players_score = 0
    for card in players_cards:
        players_score += card
    return players_score

#user input determines the next step in the game
def user_prompt():
    while True:
        valid_options = ["1", "2"]
        hit_me = input('\nChoose how to continue:\
                        \n"Hit me" = 1 || "Stay" = 2\n')

        if hit_me in valid_options:
            return hit_me
        else:
            print("Please choose a valid option")


def display_hands(): #during the game
    shown_dealers_hand = dealers_cards[0]
    players_score = calculate_player_score() #calculates player score, returned to players_score
    print(f"Players hand: {players_cards}   Total hand value: {players_score}") #prints both of the players cards
    print(f"Dealers hand: {shown_dealers_hand}") #need to make this print like a list eg. [1]

# def display_final_hand(): #displayed at the end when a winner is decided.

#Initial dealing of cards
def first_hand():     
    clear()
    print(banner) #blackjack banner
    while len(players_cards) != 2: #deals 2 cards
        deal_a_card()
    display_hands()



#Used all times after the first hand
def deal_hand(): 
    hit_me = user_prompt() #recursively calls this
    if hit_me == "1":
       deal_a_card()
       display_hands()




#testing
first_hand()
deal_hand()
print(dealers_cards)


#TODO make/modify function to be called when the game is over to show both players cards and totals. 
#TODO add rule for calculating ace as a 1 if total is over 21
#TODO add an input for calculate players score() maybe???


#  def display_hands(show_all_dealer_cards=False):
#     """Displays the player's and dealer's hands"""
#     if show_all_dealer_cards:
#         print(f"Dealer's hand: {dealers_cards} Total hand value: {calculate_score(dealers_cards)}")
#     else:
#         print(f"Dealer's hand: [{dealers_cards[0]}, ?]")
#     print(f"Player's hand: {players_cards} Total hand value: {calculate_score(players_cards)}")
