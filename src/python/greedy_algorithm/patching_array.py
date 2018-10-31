"""
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:

Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0

"""
class Solution:
    # 思路，遍历nums，维护一个变量miss，表示小于miss的值已经可以由当前已经遍历过的数
    # 组合得到，如果当前遍历的数在这之内那么miss的值就加上该数，如果不在这之内，就加
    # 上miss的值。举个例子方便理解，比如在6之前的数都可以找到对应的组合，那么加上6之
    # 后，12之前的数都可以找到组合，因此只需要将6以下的数的组合加上6即可。
    # 更详细的解释见：https://leetcode.com/problems/patching-array/discuss/78488/Sol
    # ution-+-explanation
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss = 1
        res = 0
        i = 0
        while miss < n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                res += 1
        return res

if __name__ == "__main__":
    nums1 = [1, 3]
    n1 = 6
    nums2 = [1, 5, 10]
    n2 = 20
    nums3 = [1, 2, 2]
    n3 = 5
    print(Solution().minPatches(nums1, n1))
    print(Solution().minPatches(nums2, n2))
    print(Solution().minPatches(nums3, n3))
