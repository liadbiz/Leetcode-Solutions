"""
description:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.


Idea:
    In general, there are two main solutions for this kind of problem.
    The first one is Kadane's algorithm that is :

    1. Initialize:
        max_so_far = max_ending_here = 0
    2. Iterate each element of array:
        (a) max_ending_here = max_ending_here + a[i]
        (b) if(max_ending_here < 0)
            max_ending_here = 0
        (c) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
    The basic implementation is function maxSubArray1().

    The idea of the algorithm is actually: if the sum so far < 0, it is inferior to start
    from now on. If you can understand the algorithm to this aspect. You can
    transfrom the code to maxSubArray3(), which is more elegant.

    The second one is dive and conquer algorithm, the process is:
    1. devide the input array into two sub array
    2. return the max of folloing three
        (1). max sum of left subarray
        (2). max sum of right subarray
        (3). max sum of subarray that across the left and right
    2.1 and 2.2 is just recursive call, the main point is how to find the max
    across sum, The idea is simple, find the maximum sum starting from mid
    point and ending at some point on left of mid, then find the maximum sum
    starting from mid + 1 and ending with sum point on right of mid + 1.
    Finally, combine the two and return.

    
    The basic implementation is function maxSubArray3().
"""
from sys import maxsize

class Solution:
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far, max_ending_here = -maxsize - 1, 0
        for i in range(len(nums)):
            max_ending_here = max_ending_here + nums[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0 :
                max_ending_here = 0
        return max_so_far

    def maxSubArray2(self, nums, l, r):
        """
        :type nums: List[int]
        :type left: int
        :tyope right: int
        :rtype: int
        """
        if l == r:
            return nums[l]
    
        m = (l + r) // 2

        return max(self.maxSubArray2(nums, l, m),
                   self.maxSubArray2(nums, m + 1, r),
                   self.maxCrossingSum(nums, l, m, r)) 

    def maxCrossingSum(self, nums, l, m, r):
        meh, max_sum_left = 0, -10000
        for i in range(m, l - 1, -1):
            meh += nums[i]
            
            if max_sum_left < meh:
                max_sum_left = meh


        meh, max_sum_right = 0, -10000
        for i in range(m + 1, r + 1):
            meh += nums[i]
            
            if max_sum_right < meh:
                max_sum_right = meh

        return max_sum_left + max_sum_right
        
    def maxSubArray3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        max_sum = 0
        for num in nums:
            max_sum = max_sum + num if max_sum > 0 else num
            result.append(max_sum)
        return max(result)

if __name__ == '__main__':
    case1 = [-2,1,-3,4,-1,2,1,-5,4]
    case2 = [-1]
    case3 = [1]
    # test Kadane's algorithm
    print(Solution().maxSubArray1(case1))
    print(Solution().maxSubArray1(case2))
    print(Solution().maxSubArray1(case3))

    # test divide and conquer algorithm
    n1 = len(case1)
    # n2 = len(case2)
    # n3 = len(case3)

    print(Solution().maxSubArray2(case1, 0, n1 - 1))
    # print(Solution().maxSubArray2(case2, 0, n2 - 1))
    # print(Solution().maxSubArray2(case3, 0, n3 - 1))
