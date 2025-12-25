#include <vector>
using namespace std;

class Solution {
private:
    // Stores the stock prices for recursive access
    vector<int> prices;

    // Recursive function to calculate max profit
    // currentDay -> index of the current day
    // holdingStock -> true if currently holding a stock, false otherwise
    int findMaxProfit(int currentDay = 0, bool holdingStock = false) {
        // 🛑 Base case: if we've processed all days, no more profit can be made
        if(currentDay == prices.size()) 
            return 0;
        
        int maxprofit = 0;

        if(holdingStock) {
            // ⏭️ Option 1: Skip today and continue holding the stock
            int skip = findMaxProfit(currentDay+1, holdingStock);

            // 💰 Option 2: Sell the stock today and continue without holding
            int sell = prices[currentDay] + findMaxProfit(currentDay+1, false);
            
            // 🔁 Choose the action that gives the maximum profit
            maxprofit = max(skip, sell);
        }
        else {
            // ⏭️ Option 1: Skip today and stay without holding stock
            int skip = findMaxProfit(currentDay+1, holdingStock);

            // 🛒 Option 2: Buy stock today and continue holding
            int buy = -prices[currentDay] + findMaxProfit(currentDay+1, true);

            // 🔁 Choose the action that gives the maximum profit
            maxprofit = max(skip, buy);
        }

        return maxprofit;
    }

public:
    int maxProfit(vector<int>& prices) {
        // 🚀 Store prices for recursive access
        this->prices = prices;    

        // Start recursion from day 0 without holding any stock
        return findMaxProfit();
    }
};