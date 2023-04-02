import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Open the JSON file
with open("coinnames.json", "r") as f:
    coin_names = json.load(f)

# Add coin symbols to a list
coin_symbols = [coin["symbol"] for coin in coin_names["popular_coins"]]

# Print out the coin names as a list
print("Enter the symbol of one of the following coins:")
for coin in coin_names["popular_coins"]:
    print(f"{coin['name']} ({coin['symbol']})")

# Ask which coin's price you want
coin_symbol = input()

# Keep asking for the coin symbol until it's entered correctly
while coin_symbol.lower() not in coin_symbols:
    coin_symbol = input(f"Please enter the symbol of one of the coins listed above:\n")

# Get the coin price from the API
url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_names['popular_coins'][coin_symbols.index(coin_symbol.lower())]['name'].replace(' ', '-').lower()}&vs_currencies=usd"
response = requests.get(url)
coin_data = json.loads(response.text)

# Print out the price information
price = coin_data[coin_names["popular_coins"][coin_symbols.index(coin_symbol.lower())]["name"].lower().replace(' ', '-')]
print(f"{coin_names['popular_coins'][coin_symbols.index(coin_symbol.lower())]['name']} price: {price['usd']} USD")

# Get the prices for the last 5 days
days = 5
graph_data = []
for i in range(days):
    date = datetime.now() - timedelta(days=i)
    date_str = date.strftime("%d-%m-%Y")
    url = f"https://api.coingecko.com/api/v3/coins/{coin_names['popular_coins'][coin_symbols.index(coin_symbol.lower())]['name'].replace(' ', '-').lower()}/history?date={date_str}"
    response = requests.get(url)
    history_data = json.loads(response.text)
    graph_data.append((date, history_data["market_data"]["current_price"]["usd"]))

# Plot the graph
plt.plot([data[0] for data in graph_data], [data[1] for data in graph_data])
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.title(f"{coin_names['popular_coins'][coin_symbols.index(coin_symbol.lower())]['name']} Price Graph (Last {days} Days)")
plt.show()
