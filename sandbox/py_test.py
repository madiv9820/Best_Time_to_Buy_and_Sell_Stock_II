import unittest
from timeout_decorator import timeout
from lab.hover.engine import pySolution

class TestPySolution(unittest.TestCase):
    def setUp(self):
        self.__testcases = (
            ([7,1,5,3,6,4], 7),
            ([1,2,3,4,5], 4),
            ([7,6,4,3,1], 0)
        )
        self.__solution = pySolution()
        return super().setUp()
    
    @timeout(0.5)
    def testCase_0(self):
        prices, expectedProfit = self.__testcases[0]
        actualProfit = self.__solution.maxProfit(prices = prices)
        self.assertEqual(actualProfit, expectedProfit)

    @timeout(0.5)
    def testCase_1(self):
        prices, expectedProfit = self.__testcases[1]
        actualProfit = self.__solution.maxProfit(prices = prices)
        self.assertEqual(actualProfit, expectedProfit)

    @timeout(0.5)
    def testCase_2(self):
        prices, expectedProfit = self.__testcases[2]
        actualProfit = self.__solution.maxProfit(prices = prices)
        self.assertEqual(actualProfit, expectedProfit)

if __name__ == '__main__': unittest.main(verbosity = 2)