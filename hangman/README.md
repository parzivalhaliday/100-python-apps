# Hangman Game
This is a simple implementation of the classic Hangman game in Python. In this game, the computer generates a random word, and the player needs to guess the word by suggesting letters one at a time. The player is allowed a maximum number of wrong guesses, and for each wrong guess, the computer draws a part of the "hanging man." If the player cannot guess the word within the allowed number of wrong guesses, the game is over, and the player loses.

![image](https://github.com/parzivalhaliday/python-apps/blob/main/hangman/image.png)

## Requirements
This game requires the `random_words` library to be installed. You can install it using the following command:


```python
pip install random_words
```

## How to Play
To play the game, simply run the `hangman.py` file using Python. The game will generate a random word, and you will see a series of underscores representing the letters in the word. You need to guess the letters one at a time by typing them into the console. If the letter is in the word, it will be revealed in the correct position. If it is not in the word, the computer will draw a part of the hanging man.

You are allowed a maximum number of wrong guesses, and if you cannot guess the word within the allowed number of wrong guesses, the game is over, and you lose. If you correctly guess all the letters in the word before the maximum number of wrong guesses, you win.

## Features
This implementation of the Hangman game includes the following features:

* The game generates a random word using the `random_words` library.
* The word is represented by a series of underscores.
* The player can guess letters one at a time.
* The game keeps track of the number of wrong guesses and draws the hanging man accordingly.
* The game ends when the player correctly guesses all the letters or reaches the maximum number of wrong guesses.
*The player is allowed to use a joker letter once if they have made five wrong guesses and have not used the joker yet.

## Acknowledgments
This Hangman game is based on the tutorial by Tech with Tim on YouTube. The ASCII art of the hanging man was taken from [here.](https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md)
