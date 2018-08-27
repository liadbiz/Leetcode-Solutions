"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

"""

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        import operator
        fre_dict = collections.Counter(nums).most_common()
        max_fre = max(fre_dict, key = operator.itemgetter(1))[1]
        def fre_sub(i):
            return len(nums) - nums.index(i) - nums[::-1].index(i)
        return min(fre_sub(i[0]) for i in fre_dict if i[1] == max_fre)
       

if __name__ == "__main__":
    nums1 = [1, 2, 2, 3, 1] 
    nums2 = [1,2,2,3,1,4,2] 
    print(Solution().findShortestSubArray(nums1))
    print(Solution().findShortestSubArray(nums2))
