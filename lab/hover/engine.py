from typing import List

class pySolution:
    def maxProfit(self, prices: List[int]) -> int:
        # 💰 Total accumulated profit from all profitable transactions
        totalProfit: int = 0
        
        # 🔄 Traverse prices from day 1 to last day
        for currentDay in range(1, len(prices)):
            
            # 📈 If today's price is higher than yesterday's,
            # take the profit (buy yesterday, sell today)
                totalProfit += (prices[currentDay] - prices[currentDay-1] 
                                if prices[currentDay] > prices[currentDay-1] else 0)
            
            # 🚫 If price drops or stays same, skip the transaction
        
        # 🏁 Final result:
        # Sum of all upward price movements
        return totalProfit