import requests
import random
import time
from capitals import capitals  # a dictionary of country-capital pairs

api_key = "api key"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Function to get the temperature and weather for a given city using OpenWeatherMap API
def get_temperature(city):
    # Construct the complete URL for API call
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    # Make the API call and get the response
    response = requests.get(complete_url)
    # Convert the response to JSON format
    data = response.json()
    # Check if the response contains valid data
    if data["cod"] != "404":
        # Extract the temperature and weather from the response data
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["main"]
        # Return the temperature and weather
        return temperature, weather
    else:
        # If the response does not contain valid data, return None values
        return None, None

# Function to get the corresponding emoji for a given weather condition
def get_weather_emoji(weather):
    if weather == "Clear":
        return "☀️  Sunny"
    elif weather == "Clouds":
        return "☁️  Cloudy"
    elif weather == "Rain":
        return "🌧️  Rainy"
    elif weather == "Thunderstorm":
        return "⛈️  Thunderstorm"
    elif weather == "Snow":
        return "❄️  Snowy"
    elif weather == "Mist" or weather == "Smoke" or weather == "Haze" or weather == "Dust" or weather == "Fog" or weather == "Sand" or weather == "Ash":
        return "🌫️  Foggy"
    else:
        return ""

# Introduction and instructions for the game
print("Welcome to the Temperature Guessing Game!")
print("How many capital city temperatures can you guess correctly in 10 questions?")
print("Let's get started!\n")

score = 0  # Initialize the score
start_time = time.time()  # Get the start time for calculating total time taken

# Loop through 10 rounds of the game
for i in range(10):
    # Pick a random country-capital pair
    country, capital = random.choice(list(capitals.items()))
    # Ask the player to guess the temperature of the capital city
    print(f"Question {i+1}: What is the temperature in {capital}?")
    guess = input("Your guess: ")
    # Get the correct temperature and weather of the capital city using OpenWeatherMap API
    correct_temperature, weather = get_temperature(capital)
    # Check if the player's guess is correct and update the score accordingly
    if guess.isdigit() and int(guess) == round(correct_temperature):
        print(f"Congratulations, you guessed correctly! {get_weather_emoji(weather)}")
        score += 1
    else:
        print(f"Sorry, the correct answer was {round(correct_temperature)}°C. {get_weather_emoji(weather)}")
    print("--------------------------")

end_time = time.time()  # Get the end time for calculating total time taken
total_time = end_time - start_time  # Calculate total time taken

# Display the final score and total time taken
print(f"Congratulations, you have completed the game! Your total score is: {score}/10")
print(f"Total time taken: {round(total_time, 2)} seconds")
