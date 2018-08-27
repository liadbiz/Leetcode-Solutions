"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

Idea:
    If we had some way of counting instances of the majority element as +1
    and instances of any other element as -1−1, summing them would make it
    obvious that the majority element is indeed the majority element.
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, c = 0, 0
        for n in nums:
            if c == 0:
                res = n
            c += (1 if n == res else -1)
        return res
        
if __name__ == "__main__":
    case1 = [3, 2, 3]
    case2 = [2,2,1,1,1,2,2]
    print(Solution().majorityElement(case1))
    print(Solution().majorityElement(case2))
