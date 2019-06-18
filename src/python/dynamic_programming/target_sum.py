"""
#494. Target Sum
source: https://leetcode-cn.com/problems/target-sum/submissions/

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

"""
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        sum_nums = sum(nums)
        if sum_nums < S or S < -sum_nums:
            return 0
        dp = [[0] * (2 * sum_nums + 1) for _ in range(n+1)]
        dp[0][sum_nums] = 1
        for i in range(n):
            for j in range(nums[i], 2*sum_nums + 1 - nums[i]):
                if dp[i][j]:
                    dp[i+1][j + nums[i]] += dp[i][j]
                    dp[i+1][j - nums[i]] += dp[i][j]
        return dp[-1][sum_nums + S]

if __name__ == "__main__":
    nums = [1,1,1,1,1]
    S = 3
    print(Solution().findTargetSumWays(nums, S))
