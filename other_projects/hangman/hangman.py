#import libraries
import random
import ASCII_art
import word_list

#ASCII art for hangman
art = ASCII_art.stages

#Define word list and import from the module
word_list = word_list.word_list

#choose random element from list and determine the word length
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)

#set game_over variable to be referenced later
game_over = False

#create lists to store all user guesses
correct_letters = []
incorrect_letters = []

#determine user lives
lives = 6

#testing code
#print(f'the word is {chosen_word}.')

#display game logo
print(ASCII_art.logo)

#create list that is the length of the chosen word and print it to console
display = []
for x in chosen_word:
    display += "_"

print(f"{' '.join(display)}")

#while loop that is essentially the game
while not game_over:

    #get user input
    guess = input("\nGuess a letter: ").lower()

    # Input validation: check if the input is a single alphabetical character
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a valid single letter.")
        continue

    # Check if the letter has already been guessed
    if guess in correct_letters or guess in incorrect_letters:
        print(f"\nYou have already guessed the letter '{guess}'. Try a different letter.")
        continue

    #If the letter at a position matches 'guess' then reveal that letter in the display at that position.
    for position in range(word_length):
        letter = chosen_word[position]

        if guess == letter:
            display[position] = guess
        
    if guess not in chosen_word and guess not in incorrect_letters:
        lives -= 1
        if lives == 0:
            print(f"You lose! The word was {chosen_word}.")
            break

    print(f"{' '.join(display)}")

    # Append the guess to the correct or incorrect list
    if guess in chosen_word:
        correct_letters.append(guess)
    else:
        incorrect_letters.append(guess)

    #print game status
    print(art[lives])
    print(f"\nCorrectly guessed letters: {correct_letters}")
    print(f"Incorrectly guessed letters: {incorrect_letters}")

    
    #determine if the game is over
    if "_" not in display:
        game_over = True
        print("You win!")