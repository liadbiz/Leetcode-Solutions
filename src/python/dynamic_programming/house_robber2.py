"""
#213 house robber2 

https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(nums):
            result = [0, nums[0]]
            for i in range(1, len(nums)):
                result.append(max(result[i-1]+nums[i], result[i]))
            return result[-1]
        if len(nums) > 1:
            return max(house_robber(nums[1:]), house_robber(nums[:-1]))
        elif nums:
            return nums[0]
        return 0

if __name__ == "__main__":
    nums = [2,3,2]
    nums2 = [1,2,3,1]
    print(Solution().rob(nums))
    print(Solution().rob(nums2))
