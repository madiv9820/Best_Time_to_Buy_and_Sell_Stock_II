#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 💰 Accumulates total profit from all profitable price increases
        int totalProfit = 0;

        // 🔄 Traverse prices from day 1 to the last day
        for(int currentDay = 1; currentDay < prices.size(); ++currentDay)
            
            // 📈 If today's price is higher than yesterday's,
            // take the profit (buy yesterday, sell today)
            // 🚫 Otherwise, skip (no profit opportunity)
            totalProfit += ((prices[currentDay] > prices[currentDay - 1]) ? 
                            prices[currentDay] - prices[currentDay - 1] : 0);
        
        // 🏁 Final result:
        // Sum of all upward price movements
        return totalProfit;
    }
};