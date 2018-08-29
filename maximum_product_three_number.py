"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

"""

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[-1] * max(nums[0] * nums[1], nums[-2] * nums[-3])


if __name__ == "__main__":
    nums1 = [-4, -3, -2, 0]
    nums2 = [-4, -3, 0, 2]
    nums3 = [-4, 0, 2, 3]
    nums4 = [-4, -3 -2, -1]
    print(Solution().maximumProduct(nums1))
    print(Solution().maximumProduct(nums2))
    print(Solution().maximumProduct(nums3))
    print(Solution().maximumProduct(nums4))
