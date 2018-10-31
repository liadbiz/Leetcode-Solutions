"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last
             index.
"""
class Solution:
    # 思路，从数组的最后一个位置出发，依次向前遍历，维护一个变量top，表示能到达最后
    # 一个位置的最小坐标，如果循环结束top为0，返回True，反之返回false。
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        top = len(nums) - 1
        i = top
        while i >= 0:
            if i + nums[i] >= top:
                top = i    
            i -= 1
        print(top)
        return False if top != 0 else True
        
        

if __name__ == "__main__":
    nums1 = [2,3,1,1,4]
    nums2 = [3,2,1,0,4]
    print(Solution().canJump(nums1))
    print(Solution().canJump(nums2))
