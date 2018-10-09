"""
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 

Example 1:

Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
 

Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
"""

class Solution:
    def stoneGame0(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return True

    def stoneGame1(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0] for i in range(n)]  
        for i in range(n):
            dp[i][i] = piles[i]
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] -
                        dp[i][i + d - 1])
        return dp[0][-1] > 0

    def stoneGame2(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(p)
        dp = p[:]
        for d in range(1, n):
            for i in range(1, n - d):
                dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i])
        return dp[0] > 0
