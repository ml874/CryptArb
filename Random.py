import requests
import datetime
import numpy as np
from itertools import chain, combinations
from coinmarketcap import Market


# Get top exchanges for currency pair
def get_top_exchanges(ticker, currency='BTC'):
    endpoint = requests.get("https://min-api.cryptocompare.com/data/top/exchanges?fsym=" + ticker.upper() +
                            '&tsym=' + currency.upper() + '&limit=100')
    endpoint = endpoint.json()

    return endpoint['Data'][0]['exchange']


# Get list of all coins
def getcoinlist():
    endpoint = requests.get('https://www.cryptocompare.com/api/data/coinlist/')
    endpoint = endpoint.json()
    # print endpoint
    # print endpoint
    # print endpoint.get('Data', {}).get('EOC', {}).get('CoinName', {})
    # print endpoint['Data']['EOC']['CoinName']
    # print endpoint
    tickers = [x for x in endpoint['Data']]
    return tickers


# Not sure
def gettopcurrencies(ticker):
    endpoint = requests.get('https://min-api.cryptocompare.com/data/top/pairs?fsym=' + ticker.upper())
    endpoint = endpoint.json()
    print endpoint
    tickers = [data['toSymbol'] for data in endpoint['Data']]
    return tickers



    # pairs = e.get_tradeable_pairs()
    # print pairs
    # for pair in pairs:
    #     print [pair[0], pair[1]]
    #     print e.get_price(pair[0], pair[1])
    #     print [pair[1], pair[0]]
    #     print e.get_price(pair[1], pair[0])
    #     break
