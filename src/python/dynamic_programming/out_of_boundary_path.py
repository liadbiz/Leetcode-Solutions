"""
#576 Out Of Boundary Path
source: https://leetcode-cn.com/problems/out-of-boundary-paths/
"""
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        paths = 1000000000 + 7
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(2)]
        for k in range(N):
            for x in range(m):
                for y in range(n):
                    dp[(k + 1) % 2][x][y] = ((1 if x == 0 else dp[k % 2][x - 1][y]) + \
                                            (1 if x == (m - 1) else dp[k % 2][x + 1][y]) + \
                                            (1 if y == 0 else dp[k % 2][x][y - 1]) + \
                                            (1 if y == (n - 1) else dp[k % 2][x][y + 1]) ) % paths
        return dp[N % 2][i][j]


if __name__ == "__main__":
    m, n, N, i, j = 2, 2, 2, 0, 0
    print(Solution().findPaths(m, n, N, i, j))
