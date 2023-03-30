from calendar import day_abbr, day_name   # Import day abbreviation and name from calendar module
import requests   # Import requests module for making HTTP requests to API
from PIL import Image, ImageDraw, ImageFont   # Import modules for image manipulation
import matplotlib.pyplot as plt   # Import module for displaying images
import seaborn as sns   # Import module for color palette

# OpenWeatherMap API key

api_key = 'api key' # https://home.openweathermap.org/api_keys

# Get city name from user input
city = input('For which city would you like to know the weather? ')

# Create URL for API query
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'

# Get weather data from API
response = requests.get(url)
data = response.json()

# Color palette
bg_color = (242, 242, 242)   # Background color in RGB format
text_color = (60, 60, 60)   # Text color in RGB format
sns.set_palette('deep')   # Set color palette for plot


# Image size
width, height = 800, 600 # Set width and height of image in pixels

# Create image object
img = Image.new('RGB', (width, height), color=bg_color) # Create new image with specified width, height and background color

# Create text object
font1 = ImageFont.truetype('arial.ttf', size=20)   # Set font for day abbreviation and date
font2 = ImageFont.truetype('arial.ttf', size=35)   # Set font for temperature, humidity and emoji
draw = ImageDraw.Draw(img)   # Create a drawing context for the image

# Write data on the image
x, y = 50, 50
for i in data['list'][:5]:
    date_time = i['dt_txt']   # Get date and time from API response
    date, time = date_time.split(' ')   # Split date and time
    desc = i['weather'][0]['description']   # Get weather description from API response
    temp = i['main']['temp']   # Get temperature from API response
    humidity = i['main']['humidity']   # Get humidity from API response

    # Select emoji based on weather
    if 'clear' in desc:
        emoji = '☀️'
    elif 'cloud' in desc:
        emoji = '☁️'
    elif 'rain' in desc:
        emoji = '🌧️'
    elif 'thunderstorm' in desc:
        emoji = '⛈️'
    elif 'snow' in desc:
        emoji = '❄️'
    else:
        emoji = ''

    # Write data on the image
    draw.text((x, y), f'{day_name}\n{date}', fill=(255, 255, 255), font=font1)
    draw.text((x+150, y), f'{temp}°C\nHumidity: {humidity}%', fill=(0, 0, 0), font=font2)


    # Leave 50 pixels gap for the next 3-hour weather forecast
    y += 100

# Show the image
plt.imshow(img)
plt.axis('off')
plt.show() 
