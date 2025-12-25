from typing import List

class pySolution:
    def maxProfit(self, prices: List[int]) -> int:
        # Recursive function to calculate max profit
        # currentDay -> current index in prices array
        # holdingStock -> True if we currently hold a stock, False otherwise
        def findMaxProfit(currentDay: int = 0, holdingStock: bool = False):
            # 🛑 Base case: if we've processed all days, no more profit can be made
            if currentDay == len(prices): 
                return 0
            
            # Initialize maximum profit for this state
            maxprofit: int = 0
            
            if holdingStock:
                # ⏭️ Option 1: Skip today and continue holding the stock
                skip: int = findMaxProfit(currentDay+1, holdingStock)
                
                # 💰 Option 2: Sell the stock today and continue without holding
                sell: int = prices[currentDay] + findMaxProfit(currentDay+1, False)
                
                # Choose the action that gives the maximum profit
                maxprofit = max(skip, sell)
            else:
                # ⏭️ Option 1: Skip today and stay without holding stock
                skip: int = findMaxProfit(currentDay+1, holdingStock)
                
                # 🛒 Option 2: Buy stock today and continue holding
                buy: int = -prices[currentDay] + findMaxProfit(currentDay+1, True)    
                
                # Choose the action that gives the maximum profit
                maxprofit = max(skip, buy)
            
            # 🔁 Return the maximum profit for this state
            return maxprofit
            
        # 🚀 Start recursion from day 0 without holding any stock
        return findMaxProfit()