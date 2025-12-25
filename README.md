## 📈 Dynamic Programming Approach

This solution uses **dynamic programming** to compute the maximum profit from buying and selling a stock on different days.

- **DP States:**
    - `maxprofit[currentDay][0]` → max profit on day 🚫 not holding a stock
    - `maxprofit[currentDay][1]` → max profit on day 📈 holding a stock

- **Approach:**
    1. 🛑 Initialize base case: after the last day, profit = 0.
    2. 🔄 Traverse days backwards to fill the DP table.
    3. ⚖️ At each day, decide to buy, sell, or skip based on the current state.
    4. 🏁 Result: max profit starting from day 0 with 🚫 no stock in hand.

- **Complexity:**
    - **⏱️ Time:** `O(n)`
    - **📦 Space:** `O(n)`
---