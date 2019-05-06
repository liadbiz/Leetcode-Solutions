"""
#221 maximal square

https://leetcode.com/problems/maximal-square/

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
class Solution:
    # 2d dp
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row_len, col_len = len(matrix), len(matrix[0]) if matrix else 0
        if row_len == 0 or col_len == 0:
            return 0
        dp = [[0] * (col_len + 1) for _ in range(row_len + 1)]
        max_len = 0
        for i in range(1, row_len + 1):
            for j in range(1, col_len + 1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
                    max_len = max(max_len, dp[i][j])
        return max_len ** 2
    
    # 1d dp
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row_len, col_len = len(matrix), len(matrix[0]) if matrix else 0
        if row_len == 0 or col_len == 0:
            return 0
        dp = [0 for _ in range(col_len + 1)]
        max_len = 0
        prev = 0
        for i in range(1, row_len + 1):
            for j in range(1, col_len + 1):
                temp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(prev, dp[j-1], dp[j]) + 1
                    max_len = max(dp[j], max_len)
                else:
                    dp[j] = 0
                prev = temp
        return max_len ** 2
    

if __name__ == "__main__":
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(Solution().maximalSquare(matrix))
