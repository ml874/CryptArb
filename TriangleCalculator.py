from Exchange import Exchange


class Triangle(object):

    def __init__(self, currency1, currency2, currency3):
        self.currency1 = currency1
        self.currency2 = currency2
        self.currency3 = currency3

    # Check if triangle exists between 3 pairs
    @staticmethod
    def triangle(pair1, pair2, pair3):
        return pair1[0] == pair3[1] and pair2[0] == pair1[1] and pair2[1] == pair3[0] \
               or pair1[0] == pair2[1] and pair2[0] == pair3[1] and pair1[1] == pair3[0]

    # Tests for Arbitrage: If r1*r2*r3 is greater than 1, there is an arbitrage condition.
    @staticmethod
    def arbitragepresent(rate1, rate2, rate3):
        return rate1 * rate2 * rate3 > 1
        # return (1/rate1) * (1/rate2) * (1/rate3) < 1


if __name__ == '__main__':
    kraken = Exchange()

    tradeable_pairs = list(kraken.get_tradeable_pairs())
    print len(tradeable_pairs)

    prices = {}
    count = 0
    for pair in tradeable_pairs:
        if count == 10:
            break
        try:
            p1 = kraken.get_price(pair[0], pair[1])
            p2 = kraken.get_price(pair[1], pair[2])
            p3 = kraken.get_price(pair[2], pair[0])
            prices[pair[1], pair[2]] = p2
            prices[pair[0], pair[1]] = p1
            prices[pair[2], pair[0]] = p3
            count += 1
            print count

            print (pair[1], pair[2]), (pair[0], pair[1]), (pair[2], pair[0]), Triangle.arbitragepresent(p1, p2, p3)
        except:
            continue
    print prices
