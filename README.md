# 🧠 Optimized Memoization Approach 
This approach solves the problem by exploring **all valid decisions** on each day while avoiding repeated calculations using **memoization**.

On every day, the algorithm decides between:
- 🛒 **Buying** the stock (if not currently holding one)
- 💵 **Selling** the stock (if already holding)
- ⏭️ **Skipping** the day and moving forward

Each state is uniquely identified by:
- 📅 `currentDay`
- 📦 `holdingStock` (whether a stock is currently held)

The result of each state is stored in a cache, ensuring that the same subproblem is never recomputed. This significantly improves performance compared to plain recursion while keeping the logic intuitive and readable.

Memory is explicitly released after computation to keep the solution efficient in long-running scenarios.

### ⏱️ Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` (recursion stack + memoization cache)
---