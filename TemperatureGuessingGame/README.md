# Temperature Guessing Game

This is a Python program that tests the player's knowledge of capital city temperatures using the OpenWeatherMap API. The game is played over 10 rounds, with each round asking the player to guess the temperature of a randomly selected capital city.

![tempguespng](https://github.com/parzivalhaliday/100-python-apps/blob/main/TemperatureGuessingGame/image.png)

# How to Play
To play the game, simply run the `temperature_guessing_game.py` file in a Python environment. The program will prompt the player to guess the temperature of a capital city, and the player can input their guess as an integer value.

If the player's guess is correct, they will be notified and their score will increase. If the player's guess is incorrect, the correct temperature and an emoji representing the current weather condition will be displayed.

At the end of the game, the player's final score and the total time taken to complete the game will be displayed.

## Dependencies
This program requires the following Python libraries to be installed:

`requests`

`random`

`time`

Additionally, the program imports a dictionary of country-capital pairs from the capitals.py file.

## API Key
To use the OpenWeatherMap API, you will need to obtain an API key from their website. Once you have obtained an API key, replace the `api_key` variable in the `temperature_guessing_game.py` file with your own API key.

## Acknowledgements

The program uses the OpenWeatherMap API to obtain real-time temperature data for capital cities around the world. The country-capital pairs used in the game were obtained from a public domain dataset.