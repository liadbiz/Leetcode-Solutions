"""
#120 triangle

https://leetcode.com/problems/triangle/

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n  = len(triangle)
        result = [[0] * (i + 1) for i in range(n)] 
        inf = float('inf')
        for i in range(n):
            for j in range(i + 1):
                if i == j == 0:
                    result[i][j] = triangle[i][j]
                else:
                    result[i][j] = min(result[i-1][j-1] if j != 0 else inf, result[i-1][j] if j != i else inf) + triangle[i][j]
        print(result)
        return min(result[i])

if __name__ == "__main__":
    triangle = [ [2], [3,4], [6,5,7], [4,1,8,3] ]
    print(Solution().minimumTotal(triangle))
