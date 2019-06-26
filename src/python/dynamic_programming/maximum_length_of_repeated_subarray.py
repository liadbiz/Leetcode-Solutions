"""
718. Maximum Length of Repeated Subarray
source:  https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].

"""
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)
        max_len = 0
        dp = [[0 for _ in range(m + 1)] for j in range(n + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i-1][j-1] + 1 if A[i - 1] == B[j - 1] else 0
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
        return max_len


if __name__ == "__main__":
    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    assert Solution().findLength(A, B) == 3, "result is not correct"
