#include <vector>
#include <functional>
using namespace std;

class Solution {
private:
    // 📦 Stores stock prices so they can be accessed inside recursion
    vector<int> prices;

    // 🔁 Recursive function to calculate maximum profit
    // currentDay → index of the current day
    // buyPrice  → price at which stock was bought (-1 means no stock bought yet)
    int findMaxProfit(int currentDay = 0, int buyPrice = -1) {
        // 🛑 Base case: all days processed, no more profit possible
        if (currentDay == prices.size()) 
            return 0;

        // 🧮 Possible profit values from different decisions
        int buy = 0, sell = 0, skip = 0;
        
        // ⏭️ Option 1: Skip the current day
        skip = findMaxProfit(currentDay + 1, buyPrice); 

        // 🛒 Option 2: Buy today (only if no stock is currently held)
        if (buyPrice == -1)
            buy = findMaxProfit(currentDay + 1, prices[currentDay]);

        // 💸 Option 3: Sell today (only if stock was already bought)
        else
            sell = (prices[currentDay] - buyPrice) + findMaxProfit(currentDay + 1);

        // 🏆 Return the maximum profit among all choices
        return max(skip, max(buy, sell));
    }

public:
    int maxProfit(vector<int>& prices) {
        // 🧠 Store prices for recursive access
        this->prices = prices;

        // 🚀 Start recursion from Day 0 with no stock bought
        return findMaxProfit();
    }
};