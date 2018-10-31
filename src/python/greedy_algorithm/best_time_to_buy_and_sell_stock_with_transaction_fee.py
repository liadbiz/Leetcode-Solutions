"""
Your are given an array of integers prices, for which the i-th element is the
price of a given stock on day i; and a non-negative integer fee representing a
transaction fee.

You may complete as many transactions as you like, but you need to pay the
transaction fee for each transaction. You may not buy more than 1 share of a
stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""

class Solution:
    """
    思路：用动态规划，时间复杂度是O(n)，空间复杂度是O(1)。对于每一天，都有两个状
    态一个是当前持有股票，意思就是在当天或者在当天之前的最后一个动作是买入股票，
    一个是当前不持有股票，意思是在当天或者当天之前的最后一个动作是卖掉股票。因此
    我们维护两个变量，一个是hold，代表当天的状态是持有股票时能获得的最大利润,
    这有两种情况，一个是在这之前我就买入了股票，一个是我在当天买入的股票，从动态
    规划的角度来看，就是当天的持有股票的状态可以从不持有股票的状态转移而来，也可
    以是保持之前的状态。另一个是sell，代表当天的状态是不持有股票时能获得的最大的
    利润，同样，可以从持有股票的状态转移而来，也可以是保持之前的状态。
    """
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        sell, hold = 0, -prices[0]
        for p in prices[1:]:
            sell = max(sell, hold + p - fee)
            hold = max(hold, sell - p)
        return sell


if __name__ == "__main__":
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    prices2 = [4,5,2,4,3,3,1,2,5,4]
    fee2 = 1
    print(Solution().maxProfit(prices, fee))
    print(Solution().maxProfit(prices2, fee2))

