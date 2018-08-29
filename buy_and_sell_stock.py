"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Main Idea:
    [kadane algorithm](https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%95%B0%E5%88%97%E9%97%AE%E9%A2%98)
"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit, buy = 0, prices[0]
        for p in prices:
            max_profit = max(p - buy, max_profit)
            buy = min(p, buy)
        return max_profit
            
        
if __name__ == "__main__":
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [6, 6, 4, 3, 1]
    prices3 = [1, 4, 2, 7]
    print(Solution().maxProfit(prices1))
    print(Solution().maxProfit(prices2))
    print(Solution().maxProfit(prices3))
