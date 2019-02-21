"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""
class Solution:
    # dp method
    def canPartition(self, nums: 'List[int]') -> 'bool':
        target, remainder = divmod(sum(nums), 2)
        if remainder is not 0:
            return False
        lookup = [True] + [False] * target
        for n in nums:
            for i in range(target, n - 1, -1):
                lookup[i] = lookup[i] or lookup[i - n]
        return lookup[target]

    # dp method 2, use bitset
    
    def canPartition2(self, nums: 'List[int]') -> 'bool':
        target, remainder = divmod(sum(nums), 2)
        if remainder is not 0:
            return False
        status = 1
        for n in nums:
            status = status << n | status
        return True if status >> target & 1 else False

    # backtracking method
    def canPartition3(self, nums: 'List[int]') -> 'bool':
        target, remainder = divmod(sum(nums), 2)
        if remainder or max(nums) > target:
            return False
        
        if target in nums: return True

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, g in enumerate(groups):
                if g + v <= subsum:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
            nums.append(v)
            return False 

        return search([0] * 2)

if __name__ == "__main__":
    nums = [1, 2, 3, 5]
    nums2 = [1, 10, 6, 5]
    nums3 = [1,2,3,4,5,6,7]
    # test ethod 1
    # print(Solution().canPartition(nums))
    # print(Solution().canPartition(nums2))
    # test method 2 
    # print(Solution().canPartition2(nums))
    # print(Solution().canPartition2(nums2))
    # test method 3
    print(Solution().canPartition3(nums))
    print(Solution().canPartition3(nums2))
    print(Solution().canPartition3(nums3))
