"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, 
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2,6,4,8,10]
Output: 5
You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:

1. Then length of the input array is in range [1, 10,000].
2. The input array may contain duplicates, so ascending order here means <=.

what have learned:
1. zip() function: a,Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences 
or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator 
of 1-tuples. With no arguments, it returns an empty iteratorb:

2. all() function:  Return True if all elements of the iterable are true (or if the iterable is empty).

3. array[::-1] returns the reverse order of array. array[start:end:step].
"""
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)