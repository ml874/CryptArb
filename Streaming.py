from coinmarketcap import Market
from poloniex import Poloniex
from autobahn.asyncio.wamp import ApplicationSession
from autobahn.asyncio.wamp import ApplicationRunner


class PoloniexComponent(ApplicationSession):
    def onConnect(self):
        self.join(self.config.realm)

    def onJoin(self, details):
        def onTicker(*args):
            print "Ticker event received:", args

        try:
            for x in self.subscribe(onTicker, 'ticker'):
                yield x
        except Exception as e:
            print 'Could not subscribe to topic: ', e


def main():
    runner = ApplicationRunner("wss://api.poloniex.com:443", "realm1")
    runner.run(PoloniexComponent)

if __name__ == '__main__':
    main()
    # coinmarketcap = Market()
    # coinmarketcap.ticker(currency='Ethereum', limit=3, convert='USD')
    #
    # polo = Poloniex()
    # print polo.returnChartData('BTC_ETH')

