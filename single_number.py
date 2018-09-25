"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

see my [post](http://liadbiz.github.io/leetcode-single-number-problems-summary/) of summary of singleNumber problems.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res

    
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)


if __name__ == "__main__":
    nums = [2, 2, 1]
    nums2 = [4,1,2,1,2]
    print(Solution().singleNumber(nums))
    print(Solution().singleNumber(nums2))
    print(Solution().singleNumber2(nums))
    print(Solution().singleNumber2(nums2))
