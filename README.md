# [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150)

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
- **📅 Number of days:** `1 ≤ prices.length ≤ 30,000`
- **💲 Stock price range:** `0 ≤ prices[i] ≤ 10,000`
---