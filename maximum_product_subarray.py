"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_product, max_product = 1, 1
        res = nums[0]
        for n in nums:
            p = [n, n * min_product, n * max_product]
            min_product, max_product = min(p), max(p)
            res = max(res, max_product)
        return res
        

if __name__ == "__main__":
    nums1 = [ 2, 3, -2, 4 ] 
    nums2 = [ -2, 0, -1 ] 
    print(Solution().maxProduct(nums1))    
    print(Solution().maxProduct(nums2))    

