"""
#764 largest plus sign
source: https://leetcode-cn.com/problems/largest-plus-sign/

In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000
Example 1:

Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.
Example 2:

Input: N = 2, mines = []
Output: 1
Explanation:
There is no plus sign of order 2, but there is of order 1.
Example 3:

Input: N = 1, mines = [[0, 0]]
Output: 0
Explanation:
There is no plus sign, so return 0.

"""
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        lookup = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in range(N)]
        nums = [[1] * N for _ in range(N)]
        for m1, m2 in mines:
            nums[m1][m2] = 0
        result = 0
        for i in range(N):
            l = 0
            for j in range(N):
                l = 0 if not nums[i][j] else l+1
                dp[i][j] = l
            l = 0
            for j in reversed(range(N)):
                l = 0 if not nums[i][j] else l+1
                dp[i][j] = min(dp[i][j], l)

        for j in range(N):
            l = 0
            for i in range(N):
                l = 0 if not nums[i][j] else l+1
                dp[i][j] = min(dp[i][j], l)
            l = 0
            for i in reversed(range(N)):
                l = 0 if not nums[i][j] else l+1
                dp[i][j] = min(dp[i][j], l)
                result = max(result, dp[i][j])
        return result


if __name__ == "__main__":
    N = 5
    mines = [[4,2]]
    assert Solution().orderOfLargestPlusSign(N, mines)
