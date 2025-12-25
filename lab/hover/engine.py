from typing import List

class pySolution:
    def maxProfit(self, prices: List[int]) -> int:
        # 📊 Total number of days
        n: int = len(prices)
        
        # 🧠 DP table:
        # maxprofit[day][0] → max profit on 'day' when NOT holding any stock
        # maxprofit[day][1] → max profit on 'day' when HOLDING a stock
        maxprofit: List[List[int]] = [[-1, -1] for _ in range(n+1)]
        
        # 🛑 Base case:
        # On day 'n' (after last day), no more transactions possible
        # Profit is 0 whether we are holding or not
        maxprofit[n][0] = maxprofit[n][1] = 0

        # 🔄 Traverse days backwards (Bottom-Up DP)
        for currentDay in range(n-1, -1, -1):
            
            # 🚫 NOT holding stock on currentDay
            # Option 1️⃣: Skip today → stay not holding
            # Option 2️⃣: Buy today → move to holding state (profit - price)
            maxprofit[currentDay][0] = max(
                maxprofit[currentDay+1][0], 
                maxprofit[currentDay+1][1] - prices[currentDay]
            )
            
            # 📈 HOLDING stock on currentDay
            # Option 1️⃣: Skip today → keep holding
            # Option 2️⃣: Sell today → move to not holding state (profit + price)
            maxprofit[currentDay][1] = max(
                maxprofit[currentDay+1][1],
                maxprofit[currentDay+1][0] + prices[currentDay]
            )
        
        # 🏁 Final answer:
        # Start from day 0 with NO stock in hand
        result: int = maxprofit[0][0]
        
        # 🧹 Cleanup (optional, helps memory clarity)
        del maxprofit

        # ✅ Return maximum achievable profit
        return result