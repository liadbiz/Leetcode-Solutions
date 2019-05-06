"""
Unique Binary Search Tree
Source: https://leetcode.com/problems/unique-binary-search-trees/
"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1 for i in range(n + 1)]
        for i in range(1, n + 1):
            sum = 0
            for j in range(i):
                sum += dp[j] * dp[i -j -1]
            dp[i] = sum
        return dp[-1]


if __name__ == "__main__":
    n = 3
    print(Solution().numTrees(n))
