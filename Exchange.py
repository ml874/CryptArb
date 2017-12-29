import requests
import datetime
import numpy as np
from itertools import chain, combinations, permutations
from coinmarketcap import Market

"""Get Exchange Data From Different Exchanges"""

# Top 10 Coins By Volume ($)
UNIVERSE = ['BTC', 'ETH', 'XRP', 'LTC', 'ETC', 'DSH', 'USDT', 'EOS', 'BTS', 'QTUM']


class Exchange(object):

    def __init__(self, exchange='CCCAGG'):
        self.exchange = exchange

    # Get current conversion price
    def get_price(self, base, counter):
        try:
            endpoint = requests.get('https://min-api.cryptocompare.com/data/price?fsym=' + base.upper() +
                                '&tsyms=' + counter.upper() + '&e=' + self.exchange)
            price = endpoint.json()[counter]
            return price
        except:
            raise Exception("Trading Pair does not exist for this pair")
            pass


    # Grab all historical prices and turn it into a numpy array with dates
    @staticmethod
    def historicalprices(ticker, currency='BTC'):
        endpoint = requests.get('https://min-api.cryptocompare.com/data/histoday?aggregate=1&e=CCCAGG&extraParam'
                                '=CryptoCompare&fsym=' + ticker.upper() + '&limit=100000&tryConversion=false&tsym=' +
                                currency.upper())
        endpoint = endpoint.json()

        close = [data['close'] for data in endpoint['Data']]
        time = [data['time'] for data in endpoint['Data']]
        time = [datetime.datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d') for unixtime in time]

        dateandclose = np.column_stack((time, close))
        return dateandclose

    # Given a list of tickers, returns all possible trading pairs
    @staticmethod
    def get_tradeable_pairs(listoftickers=UNIVERSE):
        # return chain(*map(lambda x: combinations(listoftickers, x), range(0, len(listoftickers) + 1)))
        return combinations(listoftickers, 3)


if __name__ == '__main__':
    poloniex = Exchange('Poloniex')
    kraken = Exchange('Kraken')

    pricep = poloniex.get_price('BTC', 'USD')
    pricek = kraken.get_price('BTC', 'USD')
    print pricep
    print pricek
