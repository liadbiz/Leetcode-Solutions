# description: 
# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
# Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their 
# absolute difference is k
# 
# how to solve?
# The problem have two cases:
# 1. when diff is not zero, construct a new set whose each element is k greater than the input, and count how many
# number is the same.
# 2. when diff is zero, just need to count how many number that show more than one time.
# 
# Python technique:
# convert list to set: set(list), for example, set([1,2,3]). 
# set is like "set" in math, so it can use &, |, to do joint and union operation. for example, 
# s1 = set([1,2,3])
# s2 = set([2,3,4])
# s1 & s2 = {2,3}
# s1 | s2 = {1,2,3,4}
# 
# collections.Counter: function that take an iterable object, return a ieterable map object that contains the information
# that how many time each element shows up.  
class Solution:

    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return len(set(nums)&{n+k for n in nums}) if k>0 else sum(v>1 for v in collections.Counter(nums).values()) if k==0 else 0 
        # means:
        # if K > 0:
        #     return len(set(nums) & {n+k for n in nums})
        # elif k == 0:
        #     return sum(v > 1 for v in collections.Counter(nums).values())
        # else:
        #     return 0
