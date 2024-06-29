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

# Cards in deck and players' hands
deck = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players_cards = []
dealers_cards = []

# Clear screen function
from os import system, name

def clear():
    """Clears the screen on the console"""
    if name == "nt":
        system("cls")
    else:
        system("clear")

def deal_card(hand):
    """Deals a random card to the specified hand"""
    random_card_choice = random.choice(deck)
    hand.append(random_card_choice)

def calculate_score(hand):
    """Calculates the score of the given hand, handling aces as 1 or 11"""
    score = sum(hand)
    ace_count = hand.count(11)
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1
    return score

def user_prompt():
    """Gets input from the user to hit or stay"""
    while True:
        valid_options = ["1", "2"]
        hit_me = input('\nChoose how to continue:\n"Hit me" = 1 || "Stay" = 2\n')
        if hit_me in valid_options:
            return hit_me
        else:
            print("Please choose a valid option")

def display_hands(show_all_dealer_cards=False):
    """Displays the player's and dealer's hands"""
    if show_all_dealer_cards:
        print(f"Dealer's hand: {dealers_cards} Total hand value: {calculate_score(dealers_cards)}")
    else:
        print(f"Dealer's hand: [{dealers_cards[0]}, ?]")
    print(f"Player's hand: {players_cards} Total hand value: {calculate_score(players_cards)}")

def first_hand():
    """Initial dealing of cards"""
    clear()
    print(banner)
    while len(players_cards) < 2:
        deal_card(players_cards)
    while len(dealers_cards) < 2:
        deal_card(dealers_cards)
    display_hands()

def deal_hand():
    """Deals subsequent hands based on user input"""
    while True:
        hit_me = user_prompt()
        if hit_me == "1":
            deal_card(players_cards)
            display_hands()
            if calculate_score(players_cards) > 21:
                print("Player busts! Dealer wins.")
                return False
        else:
            while calculate_score(dealers_cards) < 17:
                deal_card(dealers_cards)
            return True

def final_display():
    """Displays the final hands and determines the winner"""
    display_hands(show_all_dealer_cards=True)
    player_score = calculate_score(players_cards)
    dealer_score = calculate_score(dealers_cards)
    if dealer_score > 21:
        print("Dealer busts! Player wins.")
    elif player_score > dealer_score:
        print("Player wins!")
    elif player_score < dealer_score:
        print("Dealer wins.")
    else:
        print("It's a tie!")

# Game loop
def play_game():
    """Main game loop"""
    first_hand()
    if deal_hand():
        final_display()

# Start the game
play_game()
