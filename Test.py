import unittest
from TriangleCalculator import Triangle


class TestTriangle(unittest.TestCase):
    def testTriangle(self):
        e = Triangle('ETH', 'BTC', 'LTC')
        self.assertEqual(e.triangle(['ETH', 'LTC'], ['BTC', 'ETH'], ['LTC', 'BTC']), True)
        self.assertEqual(e.triangle(['ETH', 'LTC'], ['LTC', 'BTC'], ['BTC', 'ETH']), True)
        self.assertEqual(e.triangle(['BTC', 'ETH'], ['LTC', 'BTC'], ['ETH', 'LTC']), True)
        self.assertEqual(e.triangle(['BTC', 'ETH'], ['ETH', 'LTC'], ['LTC', 'BTC']), True)
        self.assertEqual(e.triangle(['LTC', 'BTC'], ['ETH', 'LTC'], ['BTC', 'ETH']), True)
        self.assertEqual(e.triangle(['LTC', 'BTC'], ['BTC', 'ETH'], ['ETH', 'LTC']), True)

        self.assertEquals(e.arbitragepresent(0.8171, 1.1910, 1.4650), True)

