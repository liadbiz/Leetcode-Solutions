"""
#368 largest divisible subset
source: https://leetcode.com/problems/largest-divisible-subset/
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [[i] for i in nums]
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if not nums[i] % nums[j]:
                    dp[i] = max(dp[j] + [nums[i]], dp[i], key=len)

        return max(dp, key=len)

    

if __name__ == "__main__":
    print(Solution().)
