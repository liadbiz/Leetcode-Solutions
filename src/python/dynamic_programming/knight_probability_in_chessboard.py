"""
#688. Knight Probability in Chessboard
source: https://leetcode-cn.com/problems/knight-probability-in-chessboard/

"""
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        directions = \
            [[ 1, 2], [ 1, -2], [ 2, 1], [ 2, -1], \
             [-1, 2], [-1, -2], [-2, 1], [-2, -1]];
        dp = [[[1 for _ in range(N)] for _ in range(N)] for _ in range(2)]
        for step in range(1, K+1):
            for i in range(N):
                for j in range(N):
                    dp[step%2][i][j] = 0
                    for direction in directions:
                        rr, cc = i+direction[0], j+direction[1]
                        if 0 <= cc < N and 0 <= rr < N:
                            dp[step%2][i][j] += 0.125 * dp[(step-1)%2][rr][cc];

        return dp[K%2][r][c]



if __name__ == "__main__":
    N = 7
    K = 2
    r = 3
    c = 3
    assert Solution().knightProbability(N, K, r, c) == 0.75, "result is not correct"
