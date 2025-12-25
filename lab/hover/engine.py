from typing import List, DefaultDict
from collections import defaultdict

class pySolution:
    def maxProfit(self, prices: List[int]) -> int:
        # 🧠 Memoization cache
        # Structure:
        #   cache[currentDay][holdingStock] -> max profit from this state
        cache: DefaultDict[DefaultDict[bool]] = defaultdict(defaultdict)
        
        def findMaxProfit(currentDay: int = 0, holdingStock: bool = False):
            # 🛑 Base case: no more days left
            if currentDay == len(prices): 
                return 0

            # 🔍 Check if the current state is already computed
            if (cache.get(currentDay, None) is None or 
                cache[currentDay].get(holdingStock, None) is None):

                # 📦 Case 1: We are currently holding a stock
                if holdingStock:
                    # ⏭️ Option 1: Skip today and continue holding
                    skip: int = findMaxProfit(currentDay + 1, holdingStock)

                    # 💵 Option 2: Sell today and stop holding
                    sell: int = prices[currentDay] + findMaxProfit(currentDay + 1, False)

                    # 🧮 Store the best possible profit for this state
                    cache[currentDay][holdingStock] = max(skip, sell)

                # 🛒 Case 2: We are NOT holding any stock
                else:
                    # ⏭️ Option 1: Skip today and stay without stock
                    skip: int = findMaxProfit(currentDay + 1, holdingStock)

                    # 🛒 Option 2: Buy today (profit decreases by stock price)
                    buy: int = -prices[currentDay] + findMaxProfit(currentDay + 1, True)

                    # 🧮 Store the best possible profit for this state
                    cache[currentDay][holdingStock] = max(skip, buy)
            
            # 🔁 Return cached result to avoid recomputation
            return cache[currentDay][holdingStock]

        # 🚀 Start recursion from day 0 with no stock in hand
        result: int = findMaxProfit()

        # 🧹 Explicitly clear cache (good practice for large inputs)
        del(cache)

        return result