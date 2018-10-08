"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

see my [post](http://liadbiz.github.io/leetcode-single-number-problems-summary/) of summary of singleNumber problems.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        a = 0
        b = 0
        for num in nums:
            xor ^= num
        mask = 1
        while(xor&mask == 0):
            mask = mask << 1
        for num in nums:
            if num&mask:
                a ^= num
            else:
                b ^= num
        return [a, b]


if __name__ == "__main__":
    nums = [2, 2, 1]
    nums2 = [4,1,2,1,2]
    print(Solution().singleNumber(nums))
    print(Solution().singleNumber(nums2))
    print(Solution().singleNumber2(nums))
    print(Solution().singleNumber2(nums2))
