import requests
import krakenex

k = krakenex.API()
c = krakenex.Connection()

APIKEY = '/Wt3ycUd+gqYHGdvqAwoKOZM2e4eGg9FaEUS9jc5WKR8NeFI6/Lynjug'


endpoint = requests.get('https://api.kraken.com/0/public/Assets/info=ETH')

print endpoint.text

