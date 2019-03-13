"""
# 303

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
Accepted
128,904
Submissions
350,101


source: https://leetcode.com/problems/range-sum-query-immutable/
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums  = nums
        self.cache = dict()


    def sumRange(self, i: int, j: int) -> int:
        if not self.cache.get((i,j)):
            result = sum(self.nums[i:j+1])
            self.cache[(i, j)] = result
            return result
        return self.cache[(i,j)]



