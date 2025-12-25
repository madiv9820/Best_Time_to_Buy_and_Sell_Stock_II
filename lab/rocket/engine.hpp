#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 📊 DP table:
        // maxprofit[day][0] → max profit on 'day' when NOT holding any stock
        // maxprofit[day][1] → max profit on 'day' when HOLDING a stock
        vector<vector<int>> maxprofit = 
        vector<vector<int>> (
            prices.size() + 1, 
            vector<int>(2, 0)
        );
        
        // 🔄 Bottom-Up DP traversal (from last day to first day)
        for(int currentDay = prices.size() - 1; currentDay >= 0; --currentDay) {
            
            // 🚫 NOT holding stock on currentDay
            // Option 1️⃣: Skip today → stay not holding
            // Option 2️⃣: Buy today → switch to holding state (profit - price)
            maxprofit[currentDay][0] = max(
                maxprofit[currentDay + 1][0],
                maxprofit[currentDay + 1][1] - prices[currentDay]
            );
            
            // 📈 HOLDING stock on currentDay
            // Option 1️⃣: Skip today → keep holding
            // Option 2️⃣: Sell today → switch to not holding state (profit + price)
            maxprofit[currentDay][1] = max(
                maxprofit[currentDay + 1][1],
                maxprofit[currentDay + 1][0] + prices[currentDay]
            );
        }
        
        // 🏁 Final answer:
        // Starting from day 0 with NO stock in hand
        int result = maxprofit[0][0];
        
        // 🧹 Free memory explicitly (clear + release capacity)
        vector<vector<int>>().swap(maxprofit);

        // ✅ Return maximum achievable profit
        return result;
    }
};