# 📈 [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150)

### 📌 Problem Overview
You are given an array `prices`, where `prices[i]` represents the 📅 **stock price on the i-th day**. Your task is to determine the **maximum profit** 💰 you can achieve by trading the stock over multiple days.

- 🛒 You may **buy** and 💵 **sell** the stock on any day  
- 🔁 You can perform **multiple transactions**  
- ⚠️ You can hold **at most one stock** at any time  
- 🔄 Buying and selling on the **same day** is allowed, as long as you never hold more than one stock  

The objective is to choose the **best sequence of buy and sell operations** to maximize total profit 📈.

### 🧠 Key Insights from Examples
- 📈 Profit comes only from **price increases**  
- ⬆️ If prices always rise, holding from the first to the last day is optimal  
- ⬇️ If prices always fall, the best choice is **not to trade**  
- 🔄 In mixed price patterns, profit can be accumulated through **multiple buy–sell cycles**

### 📏 Constraints
- 📅 **Number of days:** `1 ≤ prices.length ≤ 30,000`  
- 💲 **Stock price range:** `0 ≤ prices[i] ≤ 10,000`

### 🧩 Approaches

- #### 1️⃣ 🧨 [Brute Force](https://github.com/madiv9820/Best_Time_to_Buy_and_Sell_Stock_II/tree/Approach_01-Brute_Force)
    Recursively explores all choices on each day: **buy**, **sell**, or **skip**, based on whether a stock is currently held. Returns the **maximum profit** from all possible decision paths.  

    ⚠️ Simple but inefficient due to repeated calculations.

- #### 2️⃣ 🧠 [Memoization](https://github.com/madiv9820/Best_Time_to_Buy_and_Sell_Stock_II/tree/Approach_02-Memoization)
    Uses **recursion with memoization** to avoid recalculating states. Each state is defined by **current day** and whether a stock has been **bought**. Caching improves performance over brute force.

- #### 3️⃣ 🔁 [Brute Force Optimized](https://github.com/madiv9820/Best_Time_to_Buy_and_Sell_Stock_II/tree/Approach_03-Brute_Force_Optimized)
    Refines brute force using a clear state: **current day** and whether a stock is **held**. Still explores **buy, sell, skip** decisions recursively.  

    ⚠️ Easier to reason about, but still inefficient due to overlapping subproblems.

- #### 4️⃣ 🧠⚡ [Memoization Optimized](https://github.com/madiv9820/Best_Time_to_Buy_and_Sell_Stock_II/tree/Approach_04-Memoization_Optimized)
    Combines **state clarity** with **memoization**. Each `(day, holdingStock)` state is computed once and cached, eliminating redundant recursive calls and improving runtime.

- #### 5️⃣ 📊 [Dynamic Programming](https://github.com/madiv9820/Best_Time_to_Buy_and_Sell_Stock_II/blob/Approach_05-Dynamic_Programming)
    Uses **bottom-up DP (tabulation)**. DP table tracks **max profit per day**, based on whether a stock is **held or not**. Table is filled **backwards**, and the answer starts from day `0` with **no stock in hand**.

- #### 6️⃣ ⚡📈 [Greedy](https://github.com/madiv9820/Best_Time_to_Buy_and_Sell_Stock_II/blob/Approach_06-Greedy)
    Maximizes profit by **adding all positive price differences** between consecutive days. Each upward movement is captured as profit, simulating multiple optimal buy–sell transactions.

---