"""
#837 new 21 game
source: https://leetcode-cn.com/problems/new-21-game/

Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278

"""
class Solution:
    # comlexity: O(n^2), this method is time excceded
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [1] + [0 for _ in range(N)]
        for i in range(1, N+1):
            left = max(0, i-W)
            right = min(K-1, i-1)
            for j in range(left, right+1):
                dp[i] += dp[j] / W
        return sum(dp[K:])

    # comlexity: O(n) 
    def new21Game2(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1
        dp = [1] + [0 for _ in range(N)]
        s = 1.0
        for i in range(1, N+1):
            dp[i] = s / W
            if i < K:
                s += dp[i]
            if W <= i < K + W:
                s -= dp[i-W]
        return sum(dp[K:])


if __name__ == "__main__":
    N = 21
    K = 1
    W = 10
    assert Solution().new21Game() == 0.73178, "result is not correct"
