"""
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Idea:
    The minimum moves only occur when all the element moves to the median. 
"""

class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[~i] - nums[i] for i in range(len(nums) // 2))
        # solution2, same idea.
        """
        median = sorted(nums)[len(nums) / 2]
        return sum(abs(num - median) for num in nums)
        """

    
        

if __name__ == "__main__":
    case1 = [1, 2, 3]
    print(Solution().minMoves2(case1))
