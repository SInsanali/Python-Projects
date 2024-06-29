##################################################################################################
# Created by Sam Insanali
# GitHub: https://github.com/SInsanali
##################################################################################################
# Description:
# This program is an interactive blackjack game
# The goal is to test all of the skills I've leaned up to this point.

# retrospectively, I have no idea why I used so many functions and made it so recursive
# in the end it made the code much harder to debug
# lesson learned lol
##################################################################################################
from art import banner
import random

# cards in deck and players hands
deck = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players_cards = []
dealers_cards = []

# clear screen function
from os import system, name


def clear():
    """Clears the screen on the console"""
    # for windows
    if name == "nt":
        system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        system("clear")


def calculate_score(hand):
    """Calculates the total value of a hand"""
    score = sum(hand)
    ace_count = hand.count(11)
    while score > 21 and ace_count:
        ace_count -= 1
        score -= 10
    return score


def display_hands(show_dealer_hand=False):
    """Displays the players and dealers hand"""
    player_score = calculate_score(players_cards)
    dealers_score = calculate_score(dealers_cards)

    print(f"Players hand: {players_cards}   Total hand value: {player_score}")  # prints both of the players cards

    if show_dealer_hand:  # when game is over
        print(f"Dealers hand: {dealers_cards}   Total hand value: {dealers_score}")
    else:  # when game is not over
        print(f"Dealers hand [{dealers_cards[0]}, ?]")


def first_hand():
    """Used to deal the initial hand for the game"""
    clear()
    print(banner)  # blackjack banner
    players_cards.clear()
    dealers_cards.clear()

    while len(players_cards) != 2:  # deals 2 cards for player
        random_card_choice = random.choice(deck)
        players_cards.append(random_card_choice)

    while calculate_score(dealers_cards) < 17:
        dealers_cards.append(random.choice(deck))

    display_hands()


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


def deal_card():
    players_cards.append(random.choice(deck))
    display_hands(show_dealer_hand=False)


def final_display():
    player_score = calculate_score(players_cards)
    dealers_score = calculate_score(dealers_cards)

    if player_score == 21:
        print("\nBlackjack! You win.")
    elif dealers_score == 21:
        print("\nThe dealer has blackjack, you lose.")

    if dealers_score > 21:
        print("\nThe dealer busted! You win!")
    elif player_score > 21:
        print("\nYou've busted!")

    if player_score == dealers_score:
        print("\nIt's a tie.")
    elif player_score > dealers_score and player_score <= 21:
        print("\nYou win!")
    else:
        print("\nThe dealer wins.")


def play_again_prompt():
    while True:
        valid_choices = ["1", "2"]
        play_again = input("Type '1' to play again\
                            \nType '2' to exit\n")
        if play_again in valid_choices:
            return play_again
        else:
            print("Please choose a valid choice")


def game():
    while True:
        first_hand()  # deal the first hand

        game_running = True
        while game_running:
            should_continue = user_prompt()
            if should_continue == "1":
                deal_card()
            elif should_continue == "2":
                game_running = False

        # Dealer's turn
        while calculate_score(dealers_cards) < 17:
            dealers_cards.append(random.choice(deck))

        display_hands(show_dealer_hand=True)  # Display final hands after dealer's turn
        final_display()

        play_again = play_again_prompt()
        if play_again == "2":
            print("\n\nThanks for checking out the program.\nHave a great day!")
            break


# This is it I guess...
try:
    game()
except KeyboardInterrupt:
    # Print an error message and exit cleanly
    print("\nExecution interrupted by user. Exiting program.")
