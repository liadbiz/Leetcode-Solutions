"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""
class Solution:
    # 思路： 实际上行就是找所有升序对，差值求和即可。
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        b, s = prices[0], prices[0]
        for p in prices[1:]:
            if p < s:
                res += s - b
                b = s = p
            else:
                s = p
        if s != b:
            res += s - b
        return res


    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices)
            - 1))

if __name__ == "__main__":
    prices1 = [7,1,5,3,6,4]
    prices2 = [1,2,3,4,5]
    prices3 = [7,6,4,3,1]
    print(Solution().maxProfit(prices1))
    print(Solution().maxProfit(prices2))
    print(Solution().maxProfit(prices3))
    print(Solution().maxProfit2(prices1))
    print(Solution().maxProfit2(prices2))
    print(Solution().maxProfit2(prices3))
