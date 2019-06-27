"""
#740. Delete and Earn
source: https://leetcode-cn.com/problems/delete-and-earn/
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:

Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
 

Example 2:

Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation: 
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.

"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        for n in nums:
            lookup[n] += n
        l = sorted(list(lookup.items()), key=lambda x:x[0])
        pre_k = 0
        pre_v_1, pre_v_2 = 0, 0
        pre_v_0 = 0
        for k, v in l:
            if k - 1 != pre_k:
                pre_v_0 += v
            else:
                pre_v_0 = max(pre_v_2 + v, pre_v_1)
            pre_v_1, pre_v_2 = pre_v_0, pre_v_1
            pre_k = k
        return pre_v_0
            
            
if __name__ == "__main__":
    nums = [3, 4, 2]
    assert Solution().deleteAndEarn(nums) == 6, "result is not correct"
