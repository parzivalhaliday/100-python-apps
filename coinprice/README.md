# Coin Price Tracker


This Python script retrieves the current price and the price history of a popular cryptocurrency. You can choose a cryptocurrency from a list of popular coins, and the script will fetch its current price in USD from the CoinGecko API. It will also generate a graph of the coin's price over the last 5 days.
![coinprice](https://github.com/parzivalhaliday/100-python-apps/blob/main/coinprice/image.png)


## Libraries Used

`calendar` for day abbreviations and names
`requests` for making HTTP requests to the API
`PIL` (Python Imaging Library) for creating and manipulating the image
`matplotlib` for displaying the image
`seaborn` for setting the color palette of the plot

## Code Functionality
The script first loads a list of popular coins and their symbols from a JSON file called `coinnames.json`. It then prompts the user to enter the symbol of the cryptocurrency they want to track.

If the user enters an incorrect symbol, the script will keep prompting them until they enter a valid symbol.

Once a valid symbol is entered, the script retrieves the current price of the coin from the CoinGecko API using a GET request. It then prints out the price in USD to the console.

The script then fetches the price history of the coin over the last 5 days using a loop that makes a GET request to the API for each day. The price data is stored in a list of tuples, where each tuple contains a `datetime` object and the corresponding USD price.

Finally, the script generates a graph using the `matplotlib` library that shows the price of the coin over the last 5 days.

## Instructions
To use this script, follow these steps:

1. Clone the repository to your local machine.
2. Install the required libraries by running `pip install -r requirements.txt` in your terminal or command prompt.
3. Run the script by running `py coin_price_tracker.py` in your terminal or command prompt.
4. Enter the symbol of the cryptocurrency you want to track when prompted.
5. View the current price of the coin in USD in the console, and the price history graph that is generated.

## Libraries Used
This script uses the following libraries:

`requests` 

`json`

`matplotlib`

`datetime`


## License

You can use the code however you want.