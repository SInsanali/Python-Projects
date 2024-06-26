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

def calculate_player_score():
    players_score = 0
    for card in players_cards:
        players_score += card
    #add rule for calculating ace as a 1 if it's over 21
    return players_score

def first_hand():     
    clear()
    print(banner) #blackjack banner

    while len(players_cards) != 2:
        random_card_choice = random.choice(deck)
        players_cards.append(random_card_choice)

        random_card_choice = random.choice(deck)
        dealers_cards.append(random_card_choice)
    
    shown_dealers_hand = dealers_cards[0]
    players_score = calculate_player_score() #calculates player score, returned to players_score
    print(f"Players hand: {players_cards}   Total hand value: {players_score}") #prints both of the players cards
    print(f"Dealers hand: {shown_dealers_hand}") #need to make this print like a list eg. [1]

def deal_hand():
    while True:
        valid_options = ["1", "2"]
        hit_me = input('\nChoose how to continue:\
                       \n"Hit me" = 1 || "Stay" = 2\n')

        if hit_me in valid_options:
            break
        else:
            print("Please choose a valid option")


#testing
first_hand()
deal_hand()
# print(f"test {players_cards} && {dealers_cards}")