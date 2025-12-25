## 🧠 Memoization Approach

This approach explores all valid decisions you can make on each day:
- **Buy** the stock (if you don’t already own one)
- **Sell** the stock (if you’re holding one)
- **Skip** the day and move forward

At every day, the algorithm chooses the option that gives the **maximum possible profit** in the future. To avoid recalculating the same states again and again, results are **cached using memoization**, where each state is uniquely identified by the **current day** and the **buy price**.

By storing previously computed results, the solution eliminates redundant recursion and greatly improves performance while still keeping the logic simple and intuitive.

### ⏱️ Complexity
- **Time Complexity:** `O(n²)`
- **Space Complexity:** `O(n²)` (due to memoization)
---