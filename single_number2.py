"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99


see my [post](http://liadbiz.github.io/leetcode-single-number-problems-summary/) of summary of singleNumber problems.
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x1, x2, mask = 0, 0, 0
        for i in nums:
            x2 ^= x1 & i;
            x1 ^= i;
            mask = ~(x1 & x2);
            x2 &= mask;
            x1 &= mask;
        return x1


if __name__ == "__main__":
    nums1 = [2, 2, 3, 2]
    nums2 = [0,1,0,1,0,1,99]
    print(Solution().singleNumber(nums1))
    print(Solution().singleNumber(nums2))
