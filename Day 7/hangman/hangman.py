#import libraries
import random

#ASCII are for hangman
art = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']





#generate word list
word_list = ["aardvark", "baboon", "camel"]

#choose random element from list and determind the work length
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
print(f'the word is {chosen_word}.')

#create list that is the length of the chosen word and print it to console
display = []
for x in chosen_word:
    display += "_"

print(f"{' '.join(display)}")

#while loop that is essentially the game
while not game_over:

    #get user input
    guess = input("\nGuess a letter: ").lower()

    #If the letter at a position matches 'guess' then reveal that letter in the display at that position.
    for position in range(word_length):
        letter = chosen_word[position]

        if guess == letter:
            display[position] = guess
        
    if guess not in chosen_word:
        lives -= 1
        print(art[lives])
        if lives == 0:
            print(f"You lose! The word was {chosen_word}.")
            break

    print(f"{' '.join(display)}")
   
    # Append the guess to the correct or incorrect list
    if guess in chosen_word:
        correct_letters.append(guess)
    else:
        incorrect_letters.append(guess)
    
    print(f"\nCorrectly guessed letters: {correct_letters}")
    print(f"Incorrectly guessed letters: {incorrect_letters}")
    
    #determine if the game is over
    if "_" not in display:
        game_over = True
        print("You win!")