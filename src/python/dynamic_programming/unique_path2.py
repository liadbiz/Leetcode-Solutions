"""
#63 unique path 2
https://leetcode.com/problems/unique-paths-ii/

For description see #62
but for this problem, there are some obstales in grids.
"""
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        result = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    result[i][j] == 0
                elif i == j == 0:
                    result[i][j] = 1
                else:
                    result[i][j] = (result[i-1][j] if i - 1 >= 0 else 0) + (result[i][j-1] if j - 1 >= 0 else 0)
        return result[n-1][m-1]


if __name__ == "__main__":
    obstacleGrid = [ [0,0,0], [0,1,0], [0,0,0] ]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
