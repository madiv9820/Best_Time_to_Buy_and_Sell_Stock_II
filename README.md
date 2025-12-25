# 🧠 Brute Force Recursive Approach

In this approach, we explore **every possible decision** we can make on each day to find the **maximum profit** from **at most one stock transaction**.

On every day, we have **three choices**:

- **🟡 Buy the stock** -> Only if we haven’t bought any stock yet
- **🟢 Sell the stock** -> Only if we’re currently holding a stock
- **⏭️ Skip the day** -> Do nothing and move to the next day

The recursive function **tries all valid combinations** of these actions while strictly maintaining the rule that **you must buy before you sell**.
At each step, it calculates the profit from all possible choices and returns the maximum one.

This solution is great for:
- Understanding the **decision-making process**
- Visualizing how different choices impact profit
- Building a strong foundation before moving to **optimized solutions**

⚠️ This approach is **not optimized** and is meant purely for learning and clarity.

### Complexity
- **⏱️ Time Complexity:** `O(2ⁿ)`
    
    Each day branches into multiple recursive calls, leading to exponential time.
- **🧮 Space Complexity:** `O(n)`

    Due to the recursion call stack.

---