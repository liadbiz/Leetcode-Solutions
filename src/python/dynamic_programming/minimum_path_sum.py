"""
#64 minimum path sum

https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        result = [[0] * col_len for _ in range(row_len)]
        inf = float('inf')
        for i in range(row_len):
            for j in range(col_len):
                if i == j == 0:
                    result[i][j] = grid[i][j]
                else:
                    result[i][j] = min(result[i-1][j] if i - 1 >=0 else inf, result[i][j-1] if j - 1 >= 0 else inf) + grid[i][j]
        return result[i][j]

if __name__ == "__main__":
    grid = [ [1,3,1], [1,5,1], [4,2,1] ]
    print(Solution().minPathSum(grid))
