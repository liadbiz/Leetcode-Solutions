"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

Idea:
    increamenting all but one is the same as decreamenting that one. So we only
    need to decrease each element but min to min 1 each time. So the times to
    make `nums` all the same is what we need. 
"""

class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)


if __name__ == "__main__":
    case1 = [1,2,3]
    print(Solution().minMoves(case1))
