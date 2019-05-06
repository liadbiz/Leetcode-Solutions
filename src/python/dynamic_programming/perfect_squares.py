"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]
        for i in range(1, n + 1):
            dp += min(dp[- j * j] for j in range(1, int(i ** 0.5 + 1))) + 1,
        return dp[-1]


if __name__ == "__main__":
  n = 12
  print(Solution().numSquares(n))
