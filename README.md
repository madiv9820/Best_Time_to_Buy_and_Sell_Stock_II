## 📈 Greedy Approach

This solution uses a **greedy strategy** to maximize profit when 🔓 **unlimited transactions** are allowed.

- **💡 Idea:**
    
    Capture **every upward price movement** instead of searching for a single buy-sell window.

- **🔄 How it works:**
    - Traverse prices from day `1` to the last day
    - 📈 If today’s price > yesterday’s, add the difference to total profit
    - 🚫 Skip days with no profit opportunity
- **✅ Why it works:**

    Adding all profitable rises is equivalent to executing optimal buy-sell trades at each increase.

- **⚙️ Complexity:**
    - **⏱️ Time:** `O(n)`
    - **📦 Space:** `O(1)`
---