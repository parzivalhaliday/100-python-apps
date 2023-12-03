import random
from random_words import RandomWords


rw = RandomWords()

# Welcome message and instruction
print("Welcome to Hangman game!")
print("You need to guess a word chosen by the computer.")

# Generate a random word using the RandomWords library
word = rw.random_word()

# Convert the word to a set of lowercase letters
word_letters = set(word.lower())

# Create a set of all letters in the alphabet
alphabet = set("abcdefghijklmnopqrstuvwxyz")

# Create an empty set to store used letters
used_letters = set()

# Initialize the number of wrong guesses and maximum wrong guesses allowed
wrong_guesses = 0
max_wrong_guesses = 6

# Ask the user if they want to continue playing after the game is over
continue_guess = "y"

# Flag to check if the joker letter has been used
joker_used = False

# ASCII art of the hanging man for each stage of the game
hangman_stages = ['''
    --------
    |      |
    |      
    |      
    |      
    |     
    -
''', '''
    --------
    |      |
    |      O
    |      
    |      
    |     
    -
''', '''
    --------
    |      |
    |      O
    |      |
    |      
    |     
    -
''', '''
    --------
    |      |
    |      O
    |     /|
    |      
    |     
    -
''', '''
    --------
    |      |
    |      O
    |     /|\\
    |      
    |     
    -
''', '''
    --------
    |      |
    |      O
    |     /|\\
    |     / 
    |     
    -
''', '''
    --------
    |      |
    |      O
    |     /|\\
    |     / \\
    |     
    -
''']

# Game loop
while continue_guess == "y":
    # Print the current stage of the hanging man
    print(hangman_stages[wrong_guesses])

    # Create a list of letters and underscores to represent the word
    word_list = [letter if letter in used_letters else "_" for letter in word]
    print(" ".join(word_list))

    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the alphabet and has not been used before
    if guess in alphabet - used_letters:
        # Add the guessed letter to the used letters set
        used_letters.add(guess)
        # Check if the guessed letter is in the word
        if guess in word_letters:
            # Remove the guessed letter from the set of word letters
            word_letters.remove(guess)
        else:
            # Increment the number of wrong guesses and print a message
            wrong_guesses += 1
            print("Wrong guess.")
            # Check if the maximum number of wrong guesses has been reached
            if wrong_guesses == max_wrong_guesses:
                # If so, print the final stage of the hanging man and the correct word
                print(hangman_stages[wrong_guesses])
                print("Game over. The word was", word)
                break
    # Check if the guessed letter has been used before
    elif guess in used_letters:
        print("You have already used that letter. Please try again.")
    # Check if the guessed character is not in the alphabet
    else:
        print("Invalid character. Please try again.")

    # Check if all the letters in the word have been guessed
    if not word_letters:
        print("Congratulations! You have guessed the word", word)
        break
    #If the player has made 5 wrong guesses and hasn't used the joker yet, offer the option to use it
    if wrong_guesses == 5 and not joker_used:
        continue_guess = input("Do you want to use your joker letter? (y/n): ")
        if continue_guess.lower() == "y":
            # Select a random letter from the remaining letters in the word
            joker_letter = random.choice(list(word_letters))
            used_letters.add(joker_letter)
            word_letters.remove(joker_letter)
            joker_used = True
        else:
            continue_guess = "n"
            
print("Thanks for playing Hangman game!")
