"""
#646. Maximum Length of Pair Chain
source: https://leetcode-cn.com/problems/maximum-length-of-pair-chain/submissions/

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000].

Hint: This type of problem is called interval scheduling.
"""
class Solution:
    # actually this is greedy algorithm
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        inf = float('inf')
        right = -inf
        res = 0
        for p in pairs:
            if p[0] > right:
                right = p[1]
                res += 1
        return res
    
    # dynamic programming 
    def findLongestChain2(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        n = len(pairs)
        dp = [0 for _ in range(n+1)]
        p = [0 for i in range(n)]
        for i in range(n):
            t = i
            while t >= 0:
                if pairs[t][1] < pairs[i][0]:
                    p[i] = t + 1
                    break
                t -=1
        print(p)
        for j in range(1, n+1):
            dp[j] = max(1 + dp[p[j-1]], dp[j-1])


if __name__ == "__main__":
    pairs = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]
    assert Solution().findLongestChain(pairs) == 3, "result is not correct!"
    assert Solution().findLongestChain2(pairs) == 3, "result is not correct!"
