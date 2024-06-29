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

def calculate_score(hand):
    """Caculates the total value of a hand"""
    score = 0
    for card in hand:
        score += card
    return score

def display_hands(show_dealer_hand = False):
    """Displays the players and dealers hand"""
    player_score = calculate_score(players_cards)
    dealers_score = calculate_score(dealers_cards)
    
    print(f"Players hand: {players_cards}   Total hand value: {player_score}") #prints both of the players cards
   
    if show_dealer_hand:
        print(f"Dealers hand: {dealers_cards}   Total hand value: {dealers_score}")
    else:
        print(f"Dealers hand [{dealers_cards[0]}, ?]")

def first_hand():
    """Used to deal the initial hand for the game"""
    clear()
    print(banner) #blackjack banner
    while len(players_cards) != 2: #deals 2 cards
        random_card_choice = random.choice(deck)
        players_cards.append(random_card_choice) #for player
        
        random_card_choice = random.choice(deck)
        dealers_cards.append(random_card_choice) #for dealer
    display_hands()


#user input determines the next step in the game
def user_prompt():
    """Determines if the game continues on"""
    while True:
        valid_options = ["1", "2"]
        should_continue = input('\nChoose how to continue:\
                        \n"Hit me" = 1 || "Stay" = 2\n')

        if should_continue in valid_options:
            return should_continue
        else:
            print("Please choose a valid option")

def deal_card(hand):
    if hand == "player":
        players_cards.append(random.choice(deck))
    
    while calculate_score(dealers_cards) < 16:
        dealers_cards.append(random.choice(deck))

        if calculate_score(dealers_cards) <= 17:
            break # NOTE is break used correctly here?




#Used all times after the first hand
def deal_hand():
    """Deals a card to both players"""
    should_continue = user_prompt() #recursively calls this
    if should_continue == "1":
       deal_a_card()
       display_hands()




#testing
first_hand()
deal_hand()
print(dealers_cards)


#TODO make/modify function to be called when the game is over to show both players cards and totals. 
#TODO add rule for calculating ace as a 1 if total is over 21
#TODO add an input for calculate players score() maybe???


#NOTE Dealer must hit if their hand total is 16 or less.
#NOTE Dealer must stand if their hand total is 17 or more.

#  def display_hands(show_all_dealer_cards=False):
#     """Displays the player's and dealer's hands"""
#     if show_all_dealer_cards:
#         print(f"Dealer's hand: {dealers_cards} Total hand value: {calculate_score(dealers_cards)}")
#     else:
#         print(f"Dealer's hand: [{dealers_cards[0]}, ?]")
#     print(f"Player's hand: {players_cards} Total hand value: {calculate_score(players_cards)}")
