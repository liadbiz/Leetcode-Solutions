"""
#62 unique path 
https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach 
the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""
class Solution:
    # dynamic method
    def uniquePaths(self, m: int, n: int) -> int:
        result = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    result[i][j] = 1
                else:
                    result[i][j] = (result[i-1][j] if i - 1 >= 0 else 0) + (result[i][j-1] if j - 1 >= 0 else 0)
        print(result)
        return result[n-1][m-1]


if __name__ == "__main__":
    m = 3
    n = 2
    m2 = 7
    n2 = 3
    print(Solution().uniquePaths(m, n))
    print(Solution().uniquePaths(m2, n2))
