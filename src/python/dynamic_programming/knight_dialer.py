"""
#935. Knight Dialer
source: https://leetcode-cn.com/problems/knight-dialer/
"""
class Solution:
    def knightDialer(self, N: int) -> int:
        next_number = {1: [6, 8], 2:[7, 9], 3:[4, 8], 4:[3, 9, 0], 5:[], 6:[1, 7, 0], \
                      7: [2, 6], 8: [1, 3], 9:[2, 4], 0:[4, 6]}
        dp = [10] + [0 for _ in range(N - 1)]
        prev = {i: 1 for i in range(10)}
        for i in range(1, N):
            now = {i: 0 for i in range(10)}
            for k, v in prev.items():
                for n in next_number[k]:
                    now[n] += v
            prev = now
            dp[i] = sum(list(prev.values())) % (10**9 + 7)
        return dp[-1]
         

if __name__ == "__main__":
    N = 3
    assert Solution().new21Game(N, K, W) == 46, "reuslt is not correct"
