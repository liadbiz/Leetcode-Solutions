"""
#813. Largest Sum of Averages
source: https://leetcode-cn.com/problems/largest-sum-of-averages/

We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input:
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation:
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
 

Note:

1 <= A.length <= 100.
1 <= A[i] <= 10000.
1 <= K <= A.length.
Answers within 10^-6 of the correct answer will be accepted as correct.

"""
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        accum_sum = [A[0]]
        for i in range(1, len(A)):
            accum_sum.append(A[i]+accum_sum[-1])

        dp = [[0]*len(A) for _ in range(2)]
        for k in range(1, K+1):
            for i in range(k-1, len(A)):
                if k == 1:
                    dp[k % 2][i] = float(accum_sum[i])/(i+1)
                else:
                    for j in range(k-2, i):
                        dp[k % 2][i] = \
                            max(dp[k % 2][i],
                                dp[(k-1) % 2][j] +
                                float(accum_sum[i]-accum_sum[j])/(i-j))
        return dp[K % 2][-1]


if __name__ == "__main__":
    A = [9,1,2,3,9]
    K = 3
    assert Solution().largestSumOfAverages(A, K) == 20, "result is not correct"
