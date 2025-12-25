from typing import List

class pySolution:
    def maxProfit(self, prices: List[int]) -> int:
        # 🔁 Recursive function to explore all possible decisions
        # currentDay → current day index we are processing
        # buyPrice   → price at which stock was bought (-1 means no stock bought yet)
        def findMaxProfit(currentDay: int = 0, buyPrice: int = -1) -> int:
            # 🛑 Base case: if all days are processed, no more profit can be made
            if currentDay == len(prices): 
                return 0

            # 🧮 Variables to store profit from different choices
            buy: int = 0     # Profit if we decide to buy today
            sell: int = 0    # Profit if we decide to sell today
            skip: int = 0    # Profit if we skip today

            # ⏭️ Option 1: Skip the current day and move to the next day
            skip = findMaxProfit(currentDay + 1, buyPrice)

            # 🛒 Option 2: Buy today (only if we haven't bought any stock yet)
            if buyPrice == -1:
                buy = findMaxProfit(currentDay + 1, prices[currentDay])

            # 💸 Option 3: Sell today (only if a stock was already bought)
            else:
                sell = (prices[currentDay] - buyPrice) + findMaxProfit(currentDay + 1)

            # 🏆 Return the best profit among all available choices
            return max(skip, buy, sell)
        
        # 🚀 Start recursion from Day 0 with no stock bought
        return findMaxProfit()