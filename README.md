## 🧠 Recursive Approach (Brute Force)

This approach explores **all possible actions** on each day to calculate the **maximum profit** from a single transaction:
- 🛒 **Buy** a stock (if not already holding one)
- 💵 **Sell** the stock (if currently holding)
- ⏭️ **Skip** the day

At each step, the function recursively evaluates **all future possibilities** and chooses the action that yields the **highest profit**.

The recursion continues until the **last day** is reached.
```
⚠️ Note: This solution is simple and intuitive but not optimized — it has exponential time complexity for large inputs.
```

### ⏱️ Complexity
- **Time:** `O(2ⁿ)` – each day can branch into multiple choices
- **Space:** `O(n)` – due to recursion call stack
---