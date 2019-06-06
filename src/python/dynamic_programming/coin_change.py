"""
#322 coin change
Source: https://leetcode.com/problems/coin-change/

You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.


"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = float("inf")
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            if dp[i] != inf:
                for c in coins:
                    if c + i <= amount:
                        dp[i + c] = min(dp[i + c], dp[i] + 1)
        return dp[-1] if dp[-1] != inf else -1

if __name__ == "__main__":
  coins = [2]
  amount = 3
  print(Solution().coinChange(coins, amount))
