"""
#808. Soup Servings
source: https://leetcode-cn.com/problems/soup-servings/

There are two types of soup: type A and type B. Initially we have N ml of each type of soup. There are four kinds of operations:

Serve 100 ml of soup A and 0 ml of soup B
Serve 75 ml of soup A and 25 ml of soup B
Serve 50 ml of soup A and 50 ml of soup B
Serve 25 ml of soup A and 75 ml of soup B
When we serve some soup, we give it to someone and we no longer have it.  Each turn, we will choose from the four operations with equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as we can.  We stop once we no longer have some quantity of both types of soup.

Note that we do not have the operation where all 100 ml's of soup B are used first.  

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time.

 

Example:
Input: N = 50
Output: 0.625
Explanation:
If we choose the first two operations, A will become empty first. For the third operation, A and B will become empty at the same time. For the fourth operation, B will become empty first. So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

Notes:

0 <= N <= 10^9. 
Answers within 10^-6 of the true value will be accepted as correct.

Hint: when N = 4800, the result is 0.99999. So just return 1.0 if N > 4800. Otherwise, your code will exceed time limit.
"""
class Solution:
    def soupServings(self, N: int) -> float:
        if N > 4800:
            return 1.0
        import math
        N_A, N_B = N, N
        n = math.ceil(N / 25) + 1
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[0][0] = 0.5
        for i in range(1, n):
            dp[0][i] = 1.0
        for i in range(1, n):
            for j in range(1, n):
                dp[i][j] = 0.25 * dp[i-4 if i > 4 else 0][j] + \
                            0.25 * dp[i-3 if i > 3 else 0][j - 1 if j > 1 else 0] + \
                            0.25 * dp[i-2 if i > 2 else 0][j - 2 if j > 2 else 0] + \
                            0.25 * dp[i-1 if i > 1 else 0][j - 3 if j > 3 else 0]
        return dp[-1][-1]
