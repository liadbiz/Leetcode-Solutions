#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution(object):
    # use function itertools.combinations
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        res = []
        for i in range(len(nums) + 1):
            for c in itertools.combinations(nums, i):
                res.append(list(c))
        return res
        # one lineer 
        # return [list(c) for i in range(len(nums) + 1) for c in itertools.combinations(nums, i)]

    # use recursive method 
    def subsets2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            res += [r + [i] for r in res]
        return res
    
    # use bit maniputation
    def subsets3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = 1 << len(nums)
        for i in range(n):
            tmp = []
            for j in range(len(nums)):
                if i & (1 << j):
                    tmp.append(nums[j])
            res.append(tmp)
        return res

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
    print(Solution().subsets2(nums))
    print(Solution().subsets3(nums))

