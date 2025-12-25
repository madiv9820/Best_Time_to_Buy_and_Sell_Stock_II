from typing import List, DefaultDict
from collections import defaultdict

class pySolution:
    def maxProfit(self, prices: List[int]) -> int:
        # Memoization cache:
        # cache[currentDay][buyPrice] -> maximum profit possible from this state
        cache: DefaultDict[DefaultDict[int]] = defaultdict(defaultdict)

        def findMaxProfit(currentDay: int = 0, buyPrice: int = -1):
            # 🛑 Base case:
            # If we've processed all days, no more profit can be made
            if currentDay == len(prices): 
                return 0

            # 🧠 Check if this state is already solved
            if cache.get(currentDay, None) is None or cache[currentDay].get(buyPrice, None) is None:
                # Initialize all possible actions for the current day
                buy: int = 0    # Profit if we decide to buy today
                sell: int = 0   # Profit if we decide to sell today
                skip: int = 0   # Profit if we skip today

                # ⏭️ Option 1: Skip today and move to the next day
                skip = findMaxProfit(currentDay + 1, buyPrice)

                # 🛒 Option 2: Buy today (only if we haven't bought yet)
                if buyPrice == -1:
                    buy = findMaxProfit(currentDay + 1, prices[currentDay])
                # 💰 Option 3: Sell today (only if we already bought)
                else:
                    sell = (prices[currentDay] - buyPrice) + findMaxProfit(currentDay + 1)

                # 🧾 Store the best result for this state in the cache
                cache[currentDay][buyPrice] = max(buy, sell, skip)

            # 🔁 Return the cached result for this state
            return cache[currentDay][buyPrice]

        # 🚀 Start recursion from day 0 with no stock bought
        result = findMaxProfit()

        # 🧹 Clean up cache (optional, helps free memory)
        del cache

        # ✅ Final maximum profit
        return result