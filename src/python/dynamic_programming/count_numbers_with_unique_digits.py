"""
357. Count Numbers with Unique Digits
source: Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
"""
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n < 2:
            return 10 ** n
        dp = [1, 10]
        for i in range(2, n+1):
            dp.append(dp[i-1] + (dp[i-1] - dp[i-2]) * (11-i))
        return dp[-1]


if __name__ == "__main__":
    n = 3
    print(Solution().countNumbersWithUniqueDigits(n))
