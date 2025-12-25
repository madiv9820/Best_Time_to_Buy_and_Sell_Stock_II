#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
private:
    // 📈 Stores stock prices for each day
    vector<int> prices;

    // 🧠 Memoization cache
    // cache[currentDay][holdingStock] → maximum profit from this state
    unordered_map<int, unordered_map<bool, int>> cache;

    // 🔄 Recursive function to compute max profit
    int findMaxProfit(int currentDay = 0, bool holdingStock = false) {
        // 🛑 Base case: reached the end of days
        if (currentDay == prices.size()) 
            return 0;

        // 🔍 Check if result for this state is already cached
        if (cache.find(currentDay) == cache.end() ||
            cache[currentDay].find(holdingStock) == cache[currentDay].end()) {

            // 📦 Case 1: Currently holding a stock
            if (holdingStock) {
                // ⏭️ Option 1: Skip today, continue holding
                int skip = findMaxProfit(currentDay + 1, holdingStock);

                // 💵 Option 2: Sell today and stop holding
                int sell = prices[currentDay] + findMaxProfit(currentDay + 1, false);

                // 🧮 Store the best profit for this state
                cache[currentDay][holdingStock] = max(skip, sell);
            }
            // 🛒 Case 2: Not holding any stock
            else {
                // ⏭️ Option 1: Skip today
                int skip = findMaxProfit(currentDay + 1, holdingStock);

                // 🛒 Option 2: Buy today (profit decreases by price)
                int buy = -prices[currentDay] + findMaxProfit(currentDay + 1, true);

                // 🧮 Store the best profit for this state
                cache[currentDay][holdingStock] = max(skip, buy);
            }
        }

        // 🔁 Return cached result to avoid recomputation
        return cache[currentDay][holdingStock];
    }

public:
    int maxProfit(vector<int>& prices) {
        // 📥 Copy input prices for recursive access
        this->prices = prices;

        // 🚀 Start recursion from day 0 with no stock in hand
        int result = findMaxProfit();

        // 🧹 Explicit memory cleanup (useful for long-running programs)
        vector<int>().swap(this->prices);                       // frees prices memory
        unordered_map<int, unordered_map<bool, int>>().swap(cache); // frees cache memory

        return result;
    }
};