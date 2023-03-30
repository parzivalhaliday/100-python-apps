# Weather Forecast Image Generator using OpenWeatherMap API

This Python script generates an image that displays the 3-hour weather forecast for the next five days for a user-specified city using the OpenWeatherMap API. The image includes the day abbreviation, date, temperature, humidity, and an emoji representing the weather condition.

## Libraries Used

`calendar` for day abbreviations and names
`requests` for making HTTP requests to the API
`PIL` (Python Imaging Library) for creating and manipulating the image
`matplotlib` for displaying the image
`seaborn` for setting the color palette of the plot

## API Key

An API key from OpenWeatherMap is required to access the weather data. You can obtain a free API key by creating an account on their website.

## User Input

The user is prompted to enter the name of the city for which they want to know the weather forecast.


## Output

An image is generated displaying the 3-hour weather forecast for the next five days for the specified city.
## Instructions

Install the required libraries using the following command:

*`pip install -r requirements.txt`*

Sign up for an API key from OpenWeatherMap.
Replace the `api_key` variable in the script with your API key.
Run the script and enter the city name when prompted.
The image will be displayed on the screen.
Note: This script requires an internet connection to access the API and retrieve weather data.