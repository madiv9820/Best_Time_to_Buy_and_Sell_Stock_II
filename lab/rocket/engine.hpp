#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
private:
    // 🧠 Memoization cache:
    // cache[currentDay][buyPrice] stores the maximum profit
    // achievable from this state
    unordered_map<int, unordered_map<int, int>> cache;

    // Stores the stock prices for easy access in recursion
    vector<int> prices;

    // Recursive function to compute max profit
    // currentDay -> index of the current day
    // buyPrice   -> price at which stock was bought (-1 means not bought yet)
    int findMaxProfit(int currentDay = 0, int buyPrice = -1) {
        // 🛑 Base case:
        // If we've reached the end of the prices array,
        // no more profit can be made
        if(currentDay == prices.size())
            return 0;
        
        // 🧠 Check if this state has already been computed
        if(cache.find(currentDay) == cache.end() || 
           cache[currentDay].find(buyPrice) == cache[currentDay].end()) {

            // Possible actions from the current state
            int buy = 0;   // Profit if we buy today
            int sell = 0;  // Profit if we sell today
            int skip = 0;  // Profit if we skip today

            // ⏭️ Option 1: Skip today and move to the next day
            skip = findMaxProfit(currentDay + 1, buyPrice);

            // 🛒 Option 2: Buy today (only if we haven't bought yet)
            if(buyPrice == -1)
                buy = findMaxProfit(currentDay + 1, prices[currentDay]);
            // 💰 Option 3: Sell today (only if stock was previously bought)
            else
                sell = (prices[currentDay] - buyPrice) 
                       + findMaxProfit(currentDay + 1);

            // 🧾 Store the best result for this state in the cache
            cache[currentDay][buyPrice] = max(skip, max(buy, sell));
        }

        // 🔁 Return the cached result
        return cache[currentDay][buyPrice];
    }

public:
    int maxProfit(vector<int>& prices) {
        // Store prices for recursive access
        this->prices = prices;

        // 🚀 Start recursion from day 0 with no stock bought
        return findMaxProfit();
    }
};